"""
Created by Fanghl on 2020/9/10 13:37
"""
from flask import Blueprint, jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint


# book = Blueprint('book', __name__)
from app.models.book import Book
from app.validators.forms import BookSearchForm

api = Redprint('book')


@api.route('/search')
def search():
    """
    搜索图书 模糊检索
    """
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    #  元类 创建ORM实例
    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail', methods=['GET'])
def detail(isbn):
    """
    获取书籍详情
    :param isbn:
    :return:
    """
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)