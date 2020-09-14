"""
Created by Fanghl on 2020/9/10 13:37
"""
from flask import Blueprint, jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth


# user = Blueprint('user', __name__)
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
# @auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('/get_user', methods=['GET'])
def user():
    return 'i am fanghl'