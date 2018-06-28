#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/21 8:58
# @author :shangxudong
# @File   : FlaskTest.py
# @Software: PyCharm Community Edition

from flask import Flask, request, render_template
# from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)




# 路由处理url和视图函数关系
@app.route('/', methods=['get', 'post'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['get'])
def sign_form():
    return render_template('form.html')


@app.route('/signin', methods=['post'])
def sign_in():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'password':
        return render_template('sign-ok.html', username=username)
    return render_template('form.html', message='bad username or password', username=username)

@app.route('/sxd/<name>')
def dynamic_url(name):
    return '<h1>hello,%s</h1>' % name, 400



@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def inter_server_error(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)


