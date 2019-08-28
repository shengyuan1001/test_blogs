from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response

from myapp.UserAuthentication import UserTokenAuthentication
from myarticle.filter import ArticleFilter
from myarticle.models import Article
from myarticle.serializers import ArticleSerializer
from util.errors import ParameterException


class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = (UserTokenAuthentication,)
    filter_class = ArticleFilter

    # @list_route注册一个新API，形如：/methodname/
    @list_route(methods=["POST"], serializer_class=ArticleSerializer)
    def add_article(self, request, *args, **kwargs):
        a_writer = request.data.get("a_writer")  # 获取请求体中的名称为token的参数
        a_category = request.data.get('a_category')
        a_content = request.data.get('a_content')
        Article.objects.create(a_writer=a_writer, a_category=a_category, a_content=a_content)
        data = {
            'writer': a_writer,
            'category': a_category,
            'a_content': a_content,
        }
        return Response(data)

    def list(self, request, *args, **kwargs):
        article = Article.objects.filter(a_writer=request.user)  # 查询当前登录用户的所有文章记录
        art = self.get_serializer(article, many=True)
        data = {
            'article': art.data,
        }
        return Response(data)

    @list_route(methods=["POST"], serializer_class=ArticleSerializer)
    def filters(self, request, *args, **kwargs):
        content = request.data.get('content')
        article = Article.objects.filter(a_writer=content)  # 查询当前登录用户的所有文章记录
        art = self.get_serializer(article, many=True)
        data = {
            'article': art.data,
        }
        return Response(data)
