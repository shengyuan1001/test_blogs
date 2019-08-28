#
from myarticle.models import Article

__author__ = 'bob'
__date__ = '2019/8/27 22:26'
import django_filters


#   自定义过滤类
class ArticleFilter(django_filters.rest_framework.FilterSet):
    # 接收查询字符串参数为“”的参数
    article_writer = django_filters.CharFilter(field_name='a_writer')
    article_category = django_filters.CharFilter(field_name='a_category')
    article_content = django_filters.CharFilter(field_name='a_content')

    class Meta:
        model = Article
        fields = ['article_writer', 'article_writer', 'article_writer']


class FilterArticle(object):

    def filter_w_c(self, writer, content):
        return Article.objects.filter(a_writer=writer, a_content=content)

    def filter_writer(self, writer):
        return Article.objects.filter(a_writer=writer)

    def filter_content(self, content):
        return Article.objects.filter(a_writer=content)
