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
    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))).all()
    return jsonify(books)
