"""
Created by Fanghl on 2020/9/14 10:38
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 调用validate存贮错误信息位置 form errors
            raise ParameterException(msg=self.errors)
