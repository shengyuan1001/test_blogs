#
__author__ = 'bob'
__date__ = '2019/8/26 20:34'

from rest_framework.routers import SimpleRouter
from myapp.views import UserViewSet

user_router = SimpleRouter()
user_router.register(r'auth', UserViewSet)
