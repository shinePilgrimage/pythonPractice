#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-3-10 9:53
# @Author  : ljx
# @FileName: KNN_test.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_41086238

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 读取鸢尾花数据集，header参数制定标题的行。，默认为0，没有标题用None。

data = pd.read_csv(r"C:\Users\31502\Desktop\Cpibj_HZ\AI-Learning\KNN\iris.csv", header=0)

# data.head(10)# 默认前5行
# data.tail() # 默认末尾5行
# print(data.sample(10))  # 默认随即抽取1条
# 将类别文本映射成为数值类型，class为列名，后面列名重命名
data["class"] = data["class"].map({"Iris-versicolor": 0, "Iris-setosa": 1, "Iris-virginica": 2})
# 删除 sepallength名字一列
# data.drop("sepallength", axis=1, inplace=True)
# 查看是否重复记录
# data.duplicated().any()
# 查看重复记录
# len(data)
# 删除重复记录
# data.drop_duplicates(inplace=True)
# 查看各个类别多少记录
print(data["class"].value_counts())


class KNN:
    """使用python语言实现k近邻算法。（实现分类）"""
    def __init__(self, k):
        """初始化方法
        Parameters
        -------
        k:int   邻居的个数
        """
        self.k = k

    def fit(self, X, y):
        """
        训练方法
        Parameters
        ————————
        X：类数组类型， 形状为：[样本数量，特征数量]
        待训练的样本特征（属性）
        y：类数组类型样本的数量：[样本数量]
        每个样本的目标值（标签）
        """
        # 将x转化为array数组类型
        self.X = np.asarray(X)
        self.y = np.asarray(y)

    def predict(self, X):
        """
        根据参数传递的样本，对样本进行预测
        Parameters
        -----
        X：类数组类型， 形状为：[样本数量，特征数量]
        待训练的样本特征（属性）
        Parameters
        -----
        result:数组类型
        预测的结果。
        """
        X = np.asarray(X)
        result = []
        for x in X:
            # 对于测试集中的每一个样本,依次与训练集中的所有样本求距离, axis=1表示每一行相加
            dis = np.sqrt(np.sum((x - self.X) ** 2, axis=1))
            # 返回数组排序后,每个元素在原数组(排序前的数组)中的索引
            index = dis.argsort()
            # 进行截断,之区前k个元素,[取距离最近的k个元素索引]
            index = index[:self.k]
            # 返回数组中每个元素出现的次数,元素必须是非负整数
            count = np.bincount(self.y[index])
            # 返回ndarray数组中,值最大的元素对应的索引,该索引就是我们判定的类别
            # 最大元素索引,就是出现次数最多的元素.
            result.append(count.argmax())
        return np.asarray(result)

    def predict2(self, X):
        """
        根据参数传递的样本，对样本进行预测(考虑权重,是哟个距离的倒数作为权重)
        Parameters
        -----
        X：类数组类型， 形状为：[样本数量，特征数量]
        待训练的样本特征（属性）
        Parameters
        -----
        result:数组类型
        预测的结果。
        """
        X = np.asarray(X)
        result = []
        for x in X:
            # 对于测试集中的每一个样本,依次与训练集中的所有样本求距离, axis=1表示每一行相加
            dis = np.sqrt(np.sum((x - self.X) ** 2, axis=1))
            # 返回数组排序后,每个元素在原数组(排序前的数组)中的索引
            index = dis.argsort()
            # 进行截断,之区前k个元素,[取距离最近的k个元素索引]
            index = index[:self.k]
            # 返回数组中每个元素出现的次数,元素必须是非负整数[使用weight考虑权重,权重为距离的倒数]
            count = np.bincount(self.y[index], weights=1 / dis[index])
            # 返回ndarray数组中,值最大的元素对应的索引,该索引就是我们判定的类别
            # 最大元素索引,就是出现次数最多的元素.
            result.append(count.argmax())
        return np.asarray(result)


# 提取每个类数据
t0 = data[data["class"] == 0]
t1 = data[data["class"] == 1]
t2 = data[data["class"] == 2]
# 对每个类别数据进行洗牌, 这里的random_state就是为了保证程序每次运行都分割一样的训练集和测试集
t0 = t0.sample(len(t0), random_state=0)
t1 = t1.sample(len(t1), random_state=0)
t2 = t2.sample(len(t2), random_state=0)
# 构建训练集与测试集
# 训练集特征值
train_X = pd.concat([t0.iloc[:40, :-1], t1.iloc[:40, :-1], t2.iloc[:40, :-1]], axis=0)
# 训练集目标值
train_y = pd.concat([t0.iloc[:40, -1], t1.iloc[:40, -1], t2.iloc[:40, -1]], axis=0)
# 测试集特征值
test_X = pd.concat([t0.iloc[40:, :-1], t1.iloc[40:, :-1], t2.iloc[40:, :-1]], axis=0)
# 测试集目标集
test_y = pd.concat([t0.iloc[40:, -1], t1.iloc[40:, -1], t2.iloc[40:, -1]], axis=0)
# 创建KNN对象,进行训练与测试
knn = KNN(k=3)
# 进行训练
knn.fit(train_X, train_y)
# 进行测试.获取测试的结果
result = knn.predict(test_X)
# display(result)
# display(test_y)
# display(np.sum(result == test_y))
# display(np.sum(result == test_y) / len(result))


# 默认情况下,matplot不支持中文显示,我们需要进行一下设置
# 设置字体为ie黑体,以支持中文显示
# font = fm.FontProperties(fname='/home/yys/.local/lib/python3.8/site-packages/matplotlib/mpl-data/fonts/ttf/msyh.ttf')
# 设置在中文字体时,能够正常显示负号(-)
mpl.rcParams['axes.unicode_minus'] = False
# {"Iris-versicolor":0,"Iris-setosa":1, "Iris-virginica":2}
# 设置画布大小
plt.figure(figsize=(10, 10))
# 绘制训练集数据
plt.scatter(x=t0["petal_length"][:40], y=t0["petal_width"][:40], color="r", label="Iris-versicolor")
plt.scatter(x=t1["petal_length"][:40], y=t1["petal_width"][:40], color="g", label="ris-setosa")
plt.scatter(x=t2["petal_length"][:40], y=t2["petal_width"][:40], color="b", label="Iris-virginica")
# 绘制测试集数据
right = test_X[result == test_y]
wrong = test_X[result != test_y]
plt.scatter(x=right["petal_length"], y=right["petal_width"], color="c", marker="X", label="right")
plt.scatter(x=wrong["petal_length"], y=wrong["petal_width"], color="m", marker=">", label="wrong")
plt.xlabel("花萼长度")
plt.ylabel("花瓣长度")
plt.title("KNN分析结果")
plt.legend(loc="best")
plt.show()
