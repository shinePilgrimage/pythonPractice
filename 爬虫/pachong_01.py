import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.baidu.com")
print(req)
print(req.content)

bsobj = BeautifulSoup(req.content, "lxml")
a_list = bsobj.find_all('a')  # href属性记录一个a标签指向的链接地址

text = ''
for a in a_list:
    print(a.get('href'))
    text += a.get('href') +'\n'

with open('url.txt', 'w') as f: # 在当前路径下，以写的方式打开一个名为'url.txt'，如果不存在则创建
    f.write(text)