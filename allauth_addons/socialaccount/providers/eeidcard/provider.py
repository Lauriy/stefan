import datetime
from typing import Union

from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount, Provider


class EstonianIdCardAccount(ProviderAccount):
    def to_str(self):
        return self.account.uid


class EstonianIdCardProvider(Provider):
    id = 'eeidcard'
    name = 'Estonian ID-card'
    package = 'allauth_addons.socialaccount.providers.eeidcard'
    account_class = EstonianIdCardAccount

    # def media_js(self, request):
    #     settings = self.get_settings()
    #     request_parameters = settings.get('REQUEST_PARAMETERS', {})
    #     ctx = {'request_parameters': json.dumps(request_parameters)}
    #
    #     return render_to_string('eeidcard/auth.html', ctx, RequestContext(request))
    #
    # def get_login_url(self, request, **kwargs):
    #     next_url = "'%s'" % escapejs(kwargs.get('next') or '')
    #     process = "'%s'" % escapejs(kwargs.get('process') or 'login')
    #
    #     return 'javascript:allauth.eeidcard.auth(%s, %s)' % (next_url, process)

    def extract_uid(self, data):
        person = data['person']

        # return 'id__' + person.national_id

        return person.national_id

    def extract_common_fields(self, data):
        person = data['person']

        return dict(username=person.national_id, first_name=person.first_name, last_name=person.last_name)

        # return person._asdict()

    # def extract_email_addresses(self, data):
    #     '''ret = [EmailAddress(email=data['email'],
    #                         verified=True,
    #                         primary=True)]
    #     '''
    #     ret = []
    #
    #     return ret


providers.registry.register(EstonianIdCardProvider)
