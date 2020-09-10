"""
Created by Fanghl on 2020/9/10 13:37
"""
from flask import Blueprint

from app.libs.redprint import Redprint


# book = Blueprint('book', __name__)
api = Redprint('book')


@api.route('/get_book')
def get_book():
    return 'book'
