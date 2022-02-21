#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-2-16 9:32
# @Author  : ljx
# @FileName: test_oracle.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41086238

import cx_Oracle as cx

conn = cx.connect('test1', '123456', '172.28.151.235/ORCL')
# conn = cx.connect('用户名/密码@主机ip地址/ORCL')
cr = conn.cursor()  # 创建游标
cr.execute('select * from Websites')


# data = cr.fetchone()        # 获取一条数据
# print(data)     # 打印数据
# print('\n')

rs = cr.fetchall()
for x in rs:
    print(x)

cr.close()   # 关闭游标
conn.close()   # 关闭数据库连接
