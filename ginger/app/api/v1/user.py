"""
Created by Fanghl on 2020/9/10 13:37
"""
from flask import Blueprint

from app.libs.redprint import Redprint


# user = Blueprint('user', __name__)
api = Redprint('user')


@api.route('/get_user')
def get_user():
    return 'user'