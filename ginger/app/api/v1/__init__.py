"""
Created by Fanghl on 2020/9/10 13:36
"""
from flask import Blueprint
from app.api.v1 import user, book, client


# 将红图注册入蓝图
def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1
