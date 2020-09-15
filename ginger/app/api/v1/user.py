"""
Created by Fanghl on 2020/9/10 13:37
"""
from flask import Blueprint, jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth


# user = Blueprint('user', __name__)
from app.models.user import User
from app.models.base import db

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 超权禁止
    # g -> 线程隔离
    # namedtuple
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()