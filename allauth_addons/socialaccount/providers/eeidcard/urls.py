from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^eeidcard/auth/$', views.eeidcard_auth, name='eeidcard_auth')
]
