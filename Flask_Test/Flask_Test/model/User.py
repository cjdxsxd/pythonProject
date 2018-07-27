#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/12 17:47
# Author: sxd
# File: User.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
from Flask_Test import db


class User(db.Model):
    __tablename__ = 'b_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(18))

    def __init__(self, username, password):
        self.username = username
        self.password = password


if __name__ == '__main__':
    db.create_all()