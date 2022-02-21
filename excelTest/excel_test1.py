#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-2-17 10:53
# @Author  : ljx
# @FileName: excel_test1.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41086238

"""
    学习来源 : https://www.cnblogs.com/liulinghua90/p/9935642.html
"""

# import xlrd
import pandas as pd


file_excel = pd.read_excel(r'C:\Users\31502\PycharmProjects\pythonPractice\annexes\共享系统账号信息.xlsx',
                           engine='openpyxl', sheet_name='共享系统账号信息', index_col=False)
# xlrd更新到了2.0.1版本，只支持.xls文件
# sheet1 = file_excel.('共享系统账号信息')
print(file_excel)
row_value = file_excel.head()   # 默认读取前五行的数据
print("获取到所有的值:\n{0}".format(row_value))
# dat = []   # 列表
# for a in range(file_excel.shape[0]):  # 循环读取表格内容（每次读取一行数据）
#     cells = file_excel.row_values(a)  # 每行数据赋值给cells
#     data = cells[0].astype(int)
#     dat.append(data)

# print(file_excel.shape[0])  # shape默认第一行是表头不算行数

# data = file_excel.iloc[[1, 2]].values   # 读取指定多行的话，就要在ix[]里面嵌套列表指定行数
data = file_excel.iloc[19, 1]   # 读取第一行第二列的值，这里不需要嵌套列表
# 新库名称:iloc  旧库名称:ix
print("读取指定行的数据：\n {0}".format(data))
