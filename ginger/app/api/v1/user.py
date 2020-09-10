"""
Created by Fanghl on 2020/9/10 13:37
"""
from flask import Blueprint


user = Blueprint('user', __name__)


@user.route('/v1/user/get_user')
def get_user():
    return 'user'