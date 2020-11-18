from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stefan.api.views import AllVotesViewset

router = DefaultRouter()
router.register(r'votes', AllVotesViewset, basename='Vote')

urlpatterns = [
    path('', include(router.urls)),
]