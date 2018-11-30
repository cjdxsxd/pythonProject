#!/usr/bin/env 
#  coding:utf-8
# DATE: 2018/7/25 16:15
# Author: sxd
# File: AipFace.py
# Pycharm: PyCharm
# Contact: 3360048@163.com

from aip import AipFace
import base64, json

APP_ID = '11601549'  # 人脸识别ID
API_KEY = 's6TCPsxSR3qdXk5FUr6Rcqbv'
SECRECT_KEY = 'LNq2vqQGW9kgFAwhgQ1IoSn9TlnZfVKd'
# 创建人脸检测客户端
client = AipFace(APP_ID, API_KEY, SECRECT_KEY)


def detect_face(filepath):
    # 读取图片
    with open(filepath, 'rb') as f:
        img = base64.b64encode(f.read())
        base64_img = str(img, 'utf-8')
        print(base64_img)

    imgtype = "BASE64"
    idCardNumber = ""
    name =  ""
    name2 = name.encode('utf-8').decode('latin-1')
    options = {}
    options["face_field"] = "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype"
    groupID = "group1"
    userID = "user1"
    groupIdList = "group1"
    #调用人脸检测
    result = client.detect(base64_img, imgtype, options=options)
    print(result)
    print(type(result))
    if result.get("error_code") == 0:
        rs = result.get("result")
        face_rs = rs.get("face_list")
        list_face = face_rs[0]
        quality = list_face.get("quality")
        for k,v in quality.items():
            print(k,v)
        occlusion = quality.get("occlusion")
        if occlusion.get("left_eye") <= 0.6 and occlusion.get("right_eye") <= 0.6 and occlusion.get("nose") <= 0.7 \
            and occlusion.get("mouth") <= 0.7 and occlusion.get("left_cheek") <= 0.8 and occlusion.get("right_cheek") <= 0.8 \
            and occlusion.get("chin_contour") <= 0.6 and quality.get("blur") < 0.7 and quality.get("illumination") > 40 \
            and quality.get("completeness") == 1:
            print("这是人脸")
        #     人脸添加
        #     rgs = client.addUser(base64_img, imgtype, groupID, userID)
        #     人脸更新
        #     rgs = client.updateUser(base64_img, imgtype, groupID, userID)
        #     print(type(rgs))
        #     print(rgs.get("result"))
        # 人脸搜索
        #     rs = client.search(base64_img, imgtype, groupIdList)
        #     print(rs)

            rs = client.personVerify(base64_img, imgtype, idCardNumber, name2)
            print(rs)
        else:
            print("这张图片人脸模糊，请换一张图片！")
    else:
        print("这种图片没有人脸,只有狗脸")



if __name__ == '__main__':
    filepath = "D:\\AipFace\\sxd.jpg"
    detect_face(filepath)