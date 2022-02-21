#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-3-11 10:03
# @Author  : ljx
# @FileName: KNN_test2.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41086238

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
# X = iris.data  # 特征
# y = iris.target  # 标签
# print(X)
# print(y)

# iris.data得到数据(样本特征)，columns为列即4个特征
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# 添加标签label列
df['label'] = iris.target
print(df)
