#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/6/25 16:21
# @author :shangxudong
# @File   : sendemail.py
# @Software: PyCharm Community Edition
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os


def send_email():

    msg_from = "3360048@163.com"
    msg_to = ["469820049@qq.com", "1242492872@qq.com"]
    msg_subject = "测试邮件"

    msg_attach = MIMEMultipart()
    msg_attach['From'] = msg_from
    msg_attach['To'] = ','.join(msg_to)
    msg_attach['Subject'] = msg_subject

    text_plain = MIMEText("hello ,the first email test", 'plain', 'utf-8')
    msg_attach.attach(text_plain)

    reports = os.path.join(os.getcwd(),"Results")
    lists = os.listdir(reports)
    lists.sort(key=lambda fn: os.path.getmtime(reports+"\\"+fn))
    html = os.path.join(reports, lists[-1])

    text_html = MIMEText(open(html, 'rb').read(), 'html', 'utf-8')
    text_html.add_header('Content-Disposition', 'attachment', filename='result.html')
    msg_attach.attach(text_html)

    server = smtplib.SMTP('smtp.163.com', 25)
    server.set_debuglevel(1)
    server.login('3360048@163.com', 'xxxxxx')
    server.set_debuglevel(1)
    server.sendmail(msg_from, msg_to, msg_attach.as_string())
    server.quit()


if __name__ == '__main__':
    send_email()