
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter


from .views import HelloApiView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    url(r'^hello-view/', HelloApiView.as_view()),
    url(r'', include(router.urls))
]
