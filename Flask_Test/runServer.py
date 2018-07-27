#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/7/12 16:58
# Author: sxd
# File: runServer.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

from Flask_Test import app
from Flask_Test import db


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()