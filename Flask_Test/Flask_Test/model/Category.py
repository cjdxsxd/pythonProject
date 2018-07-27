#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/12 17:47
# Author: sxd
# File: Category.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

from Flask_Test import db


class Category(db.Model):
    __tablename__ = 'b_category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(18))

    def __init__(self, title, content):
        self.title = title
        self.content = content