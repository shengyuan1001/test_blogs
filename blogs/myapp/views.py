from rest_framework import viewsets, mixins

# Create your views here.
from rest_framework.decorators import list_route
from rest_framework.response import Response

from myapp.serializers import *


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = BlogsUser.objects.all()
    serializer_class = UserSerializer

    # @list_route注册一个新API，形如：/methodname/
    @list_route(methods=["POST"], serializer_class=RegisterSerializer)
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # raise_exception=False,未通过验证，不抛出异常，返回值，继续往下执行
        # is_valid()会联动调用序列化对象的validate（）方法
        result = serializer.is_valid(raise_exception=False)
        if not result:
            raise ParameterException({"code": "1005", "msg": "注册数据未通过验证！"})

        print("serializer.data=====")
        print(type(serializer.data))
        data = serializer.register_data(serializer.data)  # 调用封装的注册方法，返回字典
        return Response(data)

    @list_route(methods=['POST'], serializer_class=LoginSerializer)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        print("登录验证的结果result=", result)
        if not result:
            raise ParameterException({"code": "1005", "msg": "登录参数错误！"})
        res = serializer.login_data(serializer.data)
        return Response(res)
