"""
Created by Fanghl on 2020/9/10 15:05
"""
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm


api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单
    # request.args.to_dict()
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
