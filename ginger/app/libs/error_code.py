"""
Created by Fanghl on 2020/9/10 20:32
"""
from app.libs.error import APIException


class ClientTypeError(APIException):
    # 400
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid param'
    error_code = 1000