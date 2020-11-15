import logging
import urllib
from collections import namedtuple

from allauth.socialaccount import providers
from allauth.socialaccount.helpers import render_authentication_error, complete_social_login
from allauth.socialaccount.models import SocialLogin
from allauth.socialaccount.providers.base import AuthError
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import NameOID
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

from .provider import EstonianIdCardProvider


def parse_cert(ssl_client_escaped_cert: str) -> namedtuple:
    cert_data = x509.load_pem_x509_certificate(urllib.parse.unquote(ssl_client_escaped_cert).encode('utf-8'),
                                               default_backend())
    given_name = cert_data.subject.get_attributes_for_oid(NameOID.GIVEN_NAME)[0].value
    surname = cert_data.subject.get_attributes_for_oid(NameOID.SURNAME)[0].value
    national_id = cert_data.subject.get_attributes_for_oid(NameOID.SERIAL_NUMBER)[0].value
    if '-' in national_id:
        # In case prefixed with a country e.g. EE-, LV-, LT-...
        national_id = national_id.split('-')[-1]

    Person = namedtuple('Person', 'first_name, last_name, national_id')

    return Person(given_name, surname, national_id)


@csrf_exempt
def eeidcard_auth(request: HttpRequest):
    verify = request.META.get('SSL_CLIENT_VERIFY', None)
    client_cert = request.META.get('SSL_CLIENT_CERT', None)

    if not verify or not client_cert:
        return render_authentication_error(request, EstonianIdCardProvider.id, error=AuthError.UNKNOWN)

    person = parse_cert(client_cert)
    if not person:
        return render_authentication_error(request, EstonianIdCardProvider.id, error=AuthError.UNKNOWN)

    login = providers.registry.by_id(EstonianIdCardProvider.id).sociallogin_from_response(request, {'person': person})
    login.username = person.national_id
    login.user.username = person.national_id
    login.user.first_name = person.first_name
    login.user.last_name = person.last_name
    login.state = SocialLogin.state_from_request(request)
    # login.person = person

    response = complete_social_login(request, login)

    return redirect('https://stefan.indoorsman.ee/admin')

    # return complete_social_login(request, login)
