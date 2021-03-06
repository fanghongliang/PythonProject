"""
Created by Fanghl on 2020/9/14 16:47
"""
from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()

with app.app_context():
    with db.auto_commit():
        #  创建超级管理员
        user = User()
        user.nickname = 'Super',
        user._password = '123456',
        user.email = '666@qq.com',
        user.auth = 2,
        db.session.add(user)
