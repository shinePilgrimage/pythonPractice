import os
path = ''
str1 = ''
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        str1 += '"%s"' % name
print(str1)