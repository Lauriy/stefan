from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

from stefan.views import EstonianIdCardView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    re_path(r'^api/v1/', include('stefan.api.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    re_path(r'accounts/eeidcard/template', EstonianIdCardView.as_view(), name='eeidcard_template'),
]
