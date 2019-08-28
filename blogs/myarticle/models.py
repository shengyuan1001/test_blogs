from django.db import models

# Create your models here.
from myapp.models import BlogsUser


class Article(models.Model):
    a_writer = models.CharField(max_length=256)
    a_time = models.DateTimeField(auto_now=True)  # 发布时间
    a_category = models.CharField(max_length=40, null=True)
    a_content = models.TextField()  # 文章内容

    class Meta:
        db_table = 'article'
