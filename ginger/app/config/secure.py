"""
Created by Fanghl on 2020/9/10 13:21
"""


# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@127.0.0.1:3306/ginger'
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@106.13.4.75:3306/ginger'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = 'this is a secret'