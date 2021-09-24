from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('auth/',include('rest_auth.urls'))
]

