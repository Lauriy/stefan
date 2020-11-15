from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from stefan.views import EstonianIdCardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url(r'accounts/eeidcard/template', EstonianIdCardView.as_view(), name='eeidcard_template'),
]