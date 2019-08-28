from django.db import models


# Create your models here.

# 创建博客用户模型
class BlogsUser(models.Model):
    u_name = models.CharField(max_length=32, unique=True)
    u_pwd = models.CharField(max_length=256)
    u_email = models.CharField(max_length=64, unique=True)
    is_active = models.BooleanField(default=False)  # 用户是否已激活
    is_delete = models.BooleanField(default=False)  # 删除标识位

    def verify_password(self, password):
        return self.u_pwd == password

    class Meta:
        db_table = 'blogs_user'
