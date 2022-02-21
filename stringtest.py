

var1 = 'hello World!'
print(var1[0:5].capitalize())

# 字符串拼接
print("已更新字符串：" + var1 + ' ' + 'ljx')
if 'e' in var1:
    print("e在变量var1中")
else:
    print("e不在变量var1中")
if 'e' not in var1:
    print("e不在变量var1中")
else:
    print("e在变量var1中")
    print("%s 在变量 %s 中" % ('e', 'var1'))

para_str = """中国
很\t大
很\n美
"""
print(para_str)
