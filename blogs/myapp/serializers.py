#
__author__ = 'bob'
__date__ = '2019/8/26 20:38'
import uuid

from django.contrib.auth.hashers import check_password, make_password
from django.core.cache import cache
from rest_framework import serializers

from myapp.models import BlogsUser
from util.errors import ParameterException


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsUser()
        fields = '__all__'


class RegisterSerializer(serializers.Serializer):
    u_name = serializers.CharField(max_length=32, min_length=3, required=True,
                                   error_messages={
                                       "max_length": "用户名过长（不能超过32个字符）！",
                                       "min_length": "用户名太短（至少3个字符）！",
                                       "required": "必须填写用户名！"
                                   })
    u_pwd = serializers.CharField(max_length=256, min_length=6, required=True)
    u_pwd2 = serializers.CharField(max_length=256, min_length=6, required=True)
    u_email = serializers.CharField(max_length=64)

    def validate(self, attrs):
        print("validate attrs type:", type(attrs))
        username = attrs.get("u_name")  # 接收用户传递的数据
        print("username=", username)
        print("用户存在吗？", BlogsUser.objects.filter(u_name=username).exists())
        if BlogsUser.objects.filter(u_name=username).exists():
            raise ParameterException({"code": "1001", "msg": "用户名已经存在，请重新注册！"})

        if attrs.get("u_pwd") != attrs.get("u_pwd2"):
            raise ParameterException({"code": "1002", "msg": "密码不一致！"})

        email = attrs.get("u_email")
        if BlogsUser.objects.filter(u_email=email).exists():
            raise ParameterException({"code": "1003", "msg": "该邮箱已经存在，请重新注册！"})

        return attrs

    def register_data(self, validated_data):
        print('register_data......')
        password = make_password(validated_data['u_pwd'])  # 对接收到的密码进行加密
        new_user = BlogsUser.objects.create(u_name=validated_data["u_name"], u_pwd=password,
                                            u_email=validated_data["u_email"])
        result = {
            "code": 1000,
            "msg": "恭喜，注册成功！",
            "user_id": new_user.id
        }
        return result


class LoginSerializer(serializers.Serializer):  # 登录序列化类
    u_name = serializers.CharField(max_length=32, min_length=3, required=True)
    u_pwd = serializers.CharField(max_length=256, min_length=6, required=True)

    def validate(self, attrs):  # 登录逻辑验证
        if not BlogsUser.objects.filter(u_name=attrs.get("u_name")).exists():
            raise ParameterException({"code": "1004", "msg": "用户名不存在！"})

        user = BlogsUser.objects.filter(u_name=attrs.get("u_name")).first()
        if not check_password(attrs.get("u_pwd"), user.u_pwd):
            raise ParameterException({"code": "1004", "msg": "用户名不存在！"})
        return attrs

    def login_data(self, validated_data):
        token = uuid.uuid4().hex  # 服务端生成token令牌
        user = BlogsUser.objects.filter(u_name=validated_data["u_name"]).first()
        cache.set(token, user.id, timeout=60 * 60 * 24)  # 将token作为缓存的key存储到缓存中，对应的value是用户id
        res = {
            "token": token
        }
        return res
