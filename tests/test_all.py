import datetime

import pytest
from django.contrib.auth.models import User

from allauth_addons.socialaccount.providers.eeidcard.views import parse_cert
from stefan.estonian_national_id import convert_to_birthdate, SEX_MALE, get_sex
from stefan.models import Party, Vote


def test_certificate_parsing():
    person = parse_cert(
        '-----BEGIN%20CERTIFICATE-----%0AMIIF1TCCA72gAwIBAgIQCIRr%2FEmJHGtZ8GZaInm4sDANBgkqhkiG9w0BAQsFADBj%0AMQswCQYDVQQGEwJFRTEiMCAGA1UECgwZQVMgU2VydGlmaXRzZWVyaW1pc2tlc2t1%0AczEXMBUGA1UEYQwOTlRSRUUtMTA3NDcwMTMxFzAVBgNVBAMMDkVTVEVJRC1TSyAy%0AMDE1MB4XDTE3MTAyNTEwMjQyNloXDTIxMDQwNTIwNTk1OVowgY8xCzAJBgNVBAYT%0AAkVFMQ8wDQYDVQQKDAZFU1RFSUQxFzAVBgNVBAsMDmF1dGhlbnRpY2F0aW9uMSAw%0AHgYDVQQDDBdFTElBUyxMQVVSSSwzOTAwNDAyMDI1MTEOMAwGA1UEBAwFRUxJQVMx%0ADjAMBgNVBCoMBUxBVVJJMRQwEgYDVQQFEwszOTAwNDAyMDI1MTB2MBAGByqGSM49%0AAgEGBSuBBAAiA2IABLXhv5lXxUVdubHVtzlpQKL4Y2nombYRQ%2B10yKN4%2Bozwakp9%0Agw91ORDVkrInDvNbv1G1Mc%2FSt5GFjguikNGDPAcksW2u01I9L9g9TL0BM6dvQXKx%0AreCuPZJvhohTDF2zt6OCAgQwggIAMAkGA1UdEwQCMAAwDgYDVR0PAQH%2FBAQDAgOI%0AMFMGA1UdIARMMEowPgYJKwYBBAHOHwEBMDEwLwYIKwYBBQUHAgEWI2h0dHBzOi8v%0Ad3d3LnNrLmVlL3JlcG9zaXRvb3JpdW0vQ1BTMAgGBgQAj3oBAjAfBgNVHREEGDAW%0AgRRsYXVyaS5lbGlhc0BlZXN0aS5lZTAdBgNVHQ4EFgQUNhG33G56MwtUSlmWIB2f%0ApoqKJmQwIAYDVR0lAQH%2FBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMEMB8GA1UdIwQY%0AMBaAFLOriLyZ1WKkhSoIzbQdcjuDckdRMGEGCCsGAQUFBwEDBFUwUzBRBgYEAI5G%0AAQUwRzBFFj9odHRwczovL3NrLmVlL2VuL3JlcG9zaXRvcnkvY29uZGl0aW9ucy1m%0Ab3ItdXNlLW9mLWNlcnRpZmljYXRlcy8TAkVOMGoGCCsGAQUFBwEBBF4wXDAnBggr%0ABgEFBQcwAYYbaHR0cDovL2FpYS5zay5lZS9lc3RlaWQyMDE1MDEGCCsGAQUFBzAC%0AhiVodHRwOi8vYy5zay5lZS9FU1RFSUQtU0tfMjAxNS5kZXIuY3J0MDwGA1UdHwQ1%0AMDMwMaAvoC2GK2h0dHA6Ly93d3cuc2suZWUvY3Jscy9lc3RlaWQvZXN0ZWlkMjAx%0ANS5jcmwwDQYJKoZIhvcNAQELBQADggIBAETpWyB930iGlHy%2FmgkLeOoPFejInkUj%0Ab0Qjk4sgmsx%2FJ2e3jSaNmv6pDQakBhNpUu4CiCorJBixL2AbV%2Fm%2BfPTXYJLOG8s0%0AZ%2FNlqyRFuIx%2B0L86FGYYUUsCj3GWHflIM%2BSA116fS2yFCAiSeIjHjBk2ouYF6xJp%0A6TJh5UW1OSRz6bSWahc73YA9di%2BwJcCU3ETJVvCEB2%2BcK89aBhS29ROcGAGImLjl%0Aozqw20Iz5x2wrKPXZGq6uN3F8bN7QQUG68c%2BKtQzyQtjOKTszFac0V%2Fma4IHDCdW%0A17ey4FgDjAAPQmqrcNVGLfY3tj6wKDuN96TrEcQbikvUpf9OL49UCruMdGNN7ic8%0Awp5ctoKGvnUkwwalFf6Ck7ekoEeBelLcQYRWe4e6t6I2bhY7RYmp%2FxzVapUmRycg%0Aa7NmBJ6BQrl%2Bn%2FlZksYjlycATClDc1a%2FY6SCXPwCJ%2BIdv5bbt%2BCxSJoqLSuHxCkr%0AXkiOjKxTTthphj2o%2FCl%2FDvdWHuGvjMAmcEMbIWHXaCtUb97SsVRwXiCRandWpuzj%0A4oZGMk0gYQP5U74Hh43IO%2F16GmNPsmW3ja%2FRmy3qeqTEsmz%2FY7lqwpsIoywCYfa5%0AZOT8Ve0qf%2BeE%2BCSj4yOsl84Spgb4WXv7CwPhz0yyoPucEqQgILhpE0Sjbp2AmXG%2B%0AofTI0%2FmEoZvE%0A-----END%20CERTIFICATE-----%0A')

    assert person.first_name == 'LAURI'
    assert person.last_name == 'ELIAS'
    assert person.national_id == '39004020251'


def test_national_id_parsing():
    national_id = '39004020251'

    assert convert_to_birthdate(national_id) == datetime.date(year=1990, month=4, day=2)
    assert get_sex(national_id) == SEX_MALE


@pytest.mark.django_db
def test_retrieve_all_votes(client, db):
    party_name = 'Eesti Reformierakond'
    party = Party.objects.create(name=party_name, code=80043147)
    user = User.objects.create(username='39004020251')
    Vote.objects.create(user=user, party=party)

    response = client.get('/api/v1/votes/')

    assert response.json()[0]['party'] == party_name
