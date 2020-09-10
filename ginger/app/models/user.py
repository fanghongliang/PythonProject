"""
Created by Fanghl on 2020/9/10 15:39
"""
from tokenize import String

from sqlalchemy import Column, Integer, SmallInteger


class User():
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

