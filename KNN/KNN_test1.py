#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-3-10 11:54
# @Author  : ljx
# @FileName: KNN_test1.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41086238

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris.data  # 特征
y = iris.target  # 标签
print(X)
print(y)
# 随机划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20, shuffle=True)
"""
    train_target: 所要划分的样本结果3
    test_size: 样本占比，如果是整数的话就是样本的数量
    random_state: ①若为None时，每次生成的数据都是随机，可能不一样 ②若为整数时，每次生成的数据都相同
    
"""
# 数据可视化
# x[:,n]或者x[n,:]  x[:,n]表示在全部数组（维）中取第n个数据，直观来说，x[:,n]就是取所有集合的第n个数据
plt.scatter(X_train[y_train == 0][:, 0], X_train[y_train == 0][:, 1], color='r')
plt.scatter(X_train[y_train == 1][:, 0], X_train[y_train == 1][:, 1], color='g')
plt.scatter(X_train[y_train == 2][:, 0], X_train[y_train == 2][:, 1], color='b')
plt.xlabel('sepal length')  # 萼片长度
plt.ylabel('sepal width')  # 萼片宽度
plt.show()

plt.scatter(X_train[y_train == 0][:, 2], X_train[y_train == 0][:, 3], color='r')
plt.scatter(X_train[y_train == 1][:, 2], X_train[y_train == 1][:, 3], color='g')
plt.scatter(X_train[y_train == 2][:, 2], X_train[y_train == 2][:, 3], color='b')
plt.xlabel('petal length')  # 花瓣长度
plt.ylabel('petal width')  # 花瓣宽度
plt.show()