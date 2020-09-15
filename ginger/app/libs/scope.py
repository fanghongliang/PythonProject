"""
Created by Fanghl on 2020/9/15 16:31
"""


class UserScope:
    allow_api = ['v1.get_user']


class AdminScope:
    allow_api = ['v1.super_get_user']

    def __init__(self):
        self.add(UserScope())

    def add(self, other):
        # 管理员合并普通用户权限
        self.allow_api = self.allow_api + other.allow_api


def is_in_scope(scope, endpoint):
    # scope()
    # globals
    # 反射
    # token 内部携带权限参数，直接判断权限
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False