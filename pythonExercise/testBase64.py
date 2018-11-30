#!/usr/bin/env 
# _*_ coding: utf-8 _*_
# DATE: 2018/11/6 16:02
# Author: sxd
# File: testBase64.py
# Pycharm: PyCharm
# Contact: 3360048@163.com


import base64
import rsa
# 用户名:密码
s = "陆洲"
stobase64 = base64.b64encode(s.encode('utf-8'))
base64tostr = str(stobase64, encoding='utf-8')
print("ssssss",stobase64)
str2 = '6ZmG5rSy'
str = base64.decode(str2)
print(str)
# pub_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDWMN1Snmz+yvjK9E/ciSZwOubuYoVR2Yw3Eil6FAQMwrFm5+89yIxqsUSW/1eB1MaQttw830Mi2G3VDN5aMXPyZDz14XYntZYgpNUP54anRzJH3dHpBP7diD5USpvF7dZI9jOMCeV3Viw6AqXSKRNaquWN7ovj7WG7+90KPK3lDQIDAQAB'
#
with open("D:\\pubkey.pem", 'r') as f:
    pub_key = f.read()
print(pub_key)

pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key.encode('utf-8'))
print(pubkey)

with open("D:\\pengyuan.txt", 'r') as f2:
    message = f2.read()

print(message)
crypt_message = rsa.encrypt(message.encode('utf-8'), pub_key=pubkey)
# str_crpyt = str(crypt_message, encoding='utf-8')
print(crypt_message)

# import rsa
# (key1, key2) = rsa.newkeys(100)#生成随机秘钥
# print(key2)