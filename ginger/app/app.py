"""
Created by Fanghl on 2020/9/10 11:53
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    return app