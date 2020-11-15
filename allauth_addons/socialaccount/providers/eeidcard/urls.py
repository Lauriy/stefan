from django.conf.urls import url

from . import views

urlpatterns = [
    url('^eeidcard/auth/$', views.eeidcard_auth, name='eeidcard_auth')
]
