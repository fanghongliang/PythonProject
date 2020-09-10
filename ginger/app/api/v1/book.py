"""
Created by Fanghl on 2020/9/10 13:37
"""
from flask import Blueprint


book = Blueprint('book', __name__)


@book.route('/v1/book/get_book')
def get_book():
    return 'book'
