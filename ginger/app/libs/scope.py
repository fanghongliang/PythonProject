"""
Created by Fanghl on 2020/9/15 16:31
"""


class Scope:
    allow_api = []

    def __add__(self, other):
        # 管理员合并普通用户权限
        # 运算符重载
        self.allow_api = self.allow_api + other.allow_api
        # set 去重
        self.allow_api = list(set(self.allow_api))
        return self


class UserScope(Scope):
    allow_api = ['v1.get_user']


class AdminScope(Scope):
    allow_api = ['v1.super_get_user']

    def __init__(self):
        self + UserScope()


class SuperScope(Scope):
    allow_api = []

    def __init__(self):
        self + UserScope() + AdminScope()


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