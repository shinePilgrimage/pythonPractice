#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-2-9 10:59
# @Author  : ljx
# @FileName: python_time.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41086238

# import pandas as pd
from datetime import datetime
# import parse

date_test = "2022年12月26日"
# print(time.strptime(date_test, '%Y年%m月%d日'))
date_test1 = date_test.replace('年', '-').replace('月', '-').replace('日', '')
date_test2 = datetime.strptime(date_test1, '%Y-%m-%d').timetuple()  # 将string格式的变量转化成datetime下的时间格式

print(date_test2)
VersionInfo = str(date_test2.tm_year) + '-' + str(date_test2.tm_mon) + '-' + str(date_test2.tm_mday)
print(VersionInfo)
print(type(VersionInfo))

date_fina = datetime.strptime(VersionInfo, '%Y-%m-%d')  # 利用strftime()获取年/月/日
year = date_fina.strftime('%Y')
month = date_fina.strftime('%m').replace('01', '一月').replace('02', '二月', 2).replace('03', '三月').replace('04', '四月').replace('05', '五月').replace('06', '六月').replace('07', '七月').replace('08', '八月').replace('09', '九月').replace('10', '十月').replace('11', '十一月').replace('12', '十二月')
day = date_fina.strftime('%d')


print(year)
print(month)
# print(day) # 06
print(date_test2.tm_mday)
