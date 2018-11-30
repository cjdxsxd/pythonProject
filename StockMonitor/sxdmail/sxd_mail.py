#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/8/22 10:57
# Author: sxd
# File: sxd_mail.py
# Pycharm: PyCharm
# Contact: 3360048@163.com
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 连接服务器
# 登录
# 发送服务请求
# 退出


def send_mail(subject):
    print("进入邮件")
    sender = '3360048@163.com'
    receiver = '469820049@qq.com'
    msg = MIMEText(subject, 'plain', 'utf-8')
    print("主题",subject)

    msg['Subject'] = '七一二价格'
    msg['From'] = sender
    msg['To'] = receiver

    mail_host = 'smtp.163.com'
    smtp = smtplib.SMTP()
    smtp.connect(mail_host, 25)
    smtp.login("3360048@163.com","421127Cjdxsxd")
    smtp.sendmail(sender, receiver, msg.as_string())



if __name__ == '__main__':
    send_mail('test')