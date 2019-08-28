from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from myapp.models import BlogsUser
from util.errors import ParameterException


class UserTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        try:
            token = request.data.get("token") if request.data.get("token") else request.query_params.get(
                "token")  # 获取请求体中的名称为token的参数
            user_id = cache.get(token)  # 获取token对应的用户id
            user = BlogsUser.objects.get(id=user_id)  # 如果用户未登录，则此处报错
            return (user, token)
        except Exception as e:
            print("用户认证异常：", e)
            raise ParameterException({"code": 1008, "msg": "您还未登录，请先登录！"})
