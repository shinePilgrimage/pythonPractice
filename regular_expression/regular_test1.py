import re

# # re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配 匹配成功返回None
#
# line = "Cats are smarter than dogs"
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

# # re.search 扫描整个字符串并返回第一个成功的匹配。
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
#
# line = "Cats are smarter than dogs"
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#     print("searchObj.group(1) : ", searchObj.group(1))
#     print("searchObj.group(2) : ", searchObj.group(2))
# else:
#     print("Nothing found!!")
# # re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。

# re.sub用于替换字符串中的匹配项。
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', '', phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)