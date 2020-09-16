"""
Created by Fanghl on 2020/9/14 10:38
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        # body 中不含有json,不触发报错
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 调用validate存贮错误信息位置 form errors
            raise ParameterException(msg=self.errors)
        return self
