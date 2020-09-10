"""
Created by Fanghl on 2020/9/10 15:05
"""
from flask import request

from ginger.app.libs.enums import ClientTypeEnum
from ginger.app.libs.redprint import Redprint
from ginger.app.validators.forms import ClientForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 注册 登录
    # 参数 校验 接收参数
    # WTForms 验证表单
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }

def __register_user_by_email():
    pass

