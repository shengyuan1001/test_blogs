#
__author__ = 'bob'
__date__ = '2019/8/27 8:27'
from rest_framework.exceptions import APIException


class ParameterException(APIException):  # 自定义异常类
    def __init__(self, msg):
        self.detail = msg
