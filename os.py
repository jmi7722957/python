import os
import pickle
from encodings import utf_8
from os import listdir, mkdir

# 读取文件
# gg=open("C:\\Users\\HP\\Documents\\python\\Jason.txt",encoding='utf_8',errors='ignore')
# print(gg.read(-1)) 

# 列举文件夹内文件名
# aa=listdir('C:\\Users\\HP\\Documents\\python')
# aa=listdir(path='.')
# print(list(aa))

# print(os.name)#当前系统名

# 写入二进制数据
# my_list = [1,2,'老王',['abc']]
# pickle_file = open('./Jason.txt','wb') #a追加w写入b二进制
# #文件名后缀无所谓
# pickle.dump(my_list,pickle_file)       
# pickle_file.close()

# 读取二进制数据
pickle_file = open('./Jason.txt','rb')#r只读b二进制
list2 = pickle.load(pickle_file)
print(list2)
