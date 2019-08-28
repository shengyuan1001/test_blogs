#
from django.forms import model_to_dict
from rest_framework.response import Response

from myapp.models import BlogsUser
from myarticle.models import Article

__author__ = 'bob'
__date__ = '2019/8/27 14:48'

from rest_framework import serializers


# 文章序列化类
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article()
        fields = '__all__'



