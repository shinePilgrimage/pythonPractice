# import ast
# import json
#
# str1 = '{ "backend":"www.oldboy.org", "record":{"server":"122.111.2.23", "weight":"20", "maxconn":30} }'
#
# str_to_dict = eval(str1)
# str_to_dict1 = ast.literal_eval(str1)
# str_to_dict2 = json.loads(str1)
#
#
# print(str_to_dict)
# print(str_to_dict1)
# print(str_to_dict2)

# import os
#
# path_all = os.path.join('C:\\Users\\31502\\Desktop\\test_old\\', 'att_id.txt')
# print(path_all)

# # 文件路径拼接
# import os
# sid = 'sid_001'
# path1 = r'C:\\Users\\31502\\Desktop\\test_old\\'
# path2 = sid
# path_all = path1 + path2
#
# print(path_all)
#
# # 文件夹操作
# def mkdir(path):
#
#     folder = os.path.exists(path)
#     if not folder:
#         os.mkdir(path)
#         print("--- new folder ---")
#         print("--- OK ---")
#     else:
#         print("--- There is this folder! ---")
#
#
# if __name__ == '__main__':
#     mkdir(path_all)

# 将双斜杠变成单斜杠
path = r'C:\\Users\\lenovo\\Desktop\\test_old\\sid.jpg'
path1 = path.replace("\\\\", "\\", 5)
print(path1)