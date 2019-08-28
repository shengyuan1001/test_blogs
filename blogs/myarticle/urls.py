#
__author__ = 'bob'
__date__ = '2019/8/27 14:46'

from rest_framework.routers import SimpleRouter
from myarticle.views import ArticleViewSet

article_router = SimpleRouter()
article_router.register(r'auth', ArticleViewSet)
