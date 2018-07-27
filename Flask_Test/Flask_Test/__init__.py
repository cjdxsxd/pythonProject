# _*_ coding: utf-8 _*_
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Flask_Test.model import User, Category
import os


#创建项目对象
app = Flask(__name__)

# 加载配置文件
app.config.from_object('Flask_Test.setting')
app.config.from_envvar('FLASKR_SETTINGS')

# 创建数据库对象
db = SQLAlchemy(app)

