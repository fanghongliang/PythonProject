"""
Created by Fanghl on 2020/9/15 16:31
"""


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        # 管理员合并普通用户权限
        # 运算符重载
        self.allow_api = self.allow_api + other.allow_api
        # set 去重
        self.allow_api = list(set(self.allow_api))
        # 红图级别权限相加
        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))
        # 逆向筛选权限
        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class UserScope(Scope):
    allow_api = ['v1.user+get_user']
    allow_module = []
    forbidden = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user',
    #              'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        # 排除 筛选视图函数
        # self + UserScope()
        pass


def is_in_scope(scope, endpoint):
    # scope()
    # globals
    # 反射
    # token 内部携带权限参数，直接判断权限
    # v1.red_name + view_func
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False