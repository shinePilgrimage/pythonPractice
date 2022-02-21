

tup1 = ('apple', 'strawberry', 'orange')  # 元组中的元素值是不允许修改的
tup2 = "a", "b", "c", "d"
tup3 = (1, 2, 3, 4, 5, 6)  # tup1 tup2 内存地址不一样了  id(tup3)
print(type(tup2))
print("tup3[0:5]:", tup3[0:5])
tup4 = tup1 + tup2  # 删除元组
print(len(tup4))
print(tup4)


