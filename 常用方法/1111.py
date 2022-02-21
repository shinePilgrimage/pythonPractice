#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-1-29 13:53
# @Author  : ljx
# @FileName: 1111.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41086238


import os
import requests
from io import BytesIO
import PIL
from PIL import Image

att_id = 'erurur'


# data = {"method":"down","view":"1","att_id":'60c663f7-9fd2-462b-8e88-c160a2c3f208'}
# r = requests.get('http://10.78.100.67/hzpt/xipAttMrgAction.do',params=data)
# f = BytesIO(r.content)
# im = Image.open(f)
# im.save("1.jpg")

def save_img(url, att_id):
    data = {"method": "down", "view": "1"}
    data['att_id'] = att_id
    path1 = 'C:\\Users\\lenovo\\Desktop\\test_old'  # 使用转义
    path2 = att_id
    path3 = '.jpg'
    path_all = path1 + os.sep + path2 + path3

    print(path_all)

    r = requests.get(url, params=data)
    f = BytesIO(r.content)
    im = Image.open(f)
    im.save(path_all)


save_img("http://10.78.100.67/hzpt/xipAttMrgAction.do", att_id)
