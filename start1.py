#列表
from calendar import c


member = ["a","ab","abc",[1,2,3],"abcde","abcdefg"]
# 遍历列表
# for i in member:
#     print(i,len(i))
#查看列表
# print(dir(member))
# .append()表尾追加一个值
# .extend()在表尾追加一个列表
# 获取某个定位
# .pop(1)
# .count(元素)  计算元素个数
# .reverse()　　元素翻转
# .sort()　　排序
# 复制列表
# la=member[:]

# 元素数组
a=1,2,3,4,5 
b="a","b","c"
# c=a[2:]+b[2:]
# print(c)
# 序列常用的方法
# list(iterable) #把一个可迭代对象转换为列表
# tuple([iterable]) #把一个可迭代对象转换为元组
# str(obj) #把obj对象转换为字符串
# print(list(enumerate(b)))#生成由每个元素的index值和item值组成的元组
# zip(a,b)#融合

# 字典
array=[4,5,6]
dic={a:123,b:"GG思密达",c:array}
print()
# dict.keys() #返回一个包含字典所有KEY的列表；
# dict.values() #返回一个包含字典所有value的列表；
# dict.items() #返回一个包含所有（键，值）元祖的列表；
# adict.clear() #删除字典中的所有项或元素；
# adict.copy() #返回一个字典浅拷贝的副本；
# dic.get(c)#获取某个字典元素
# adict.pop(c)#剪切某个元素

# 函数式编程
# Python提供函数式编程思想的函数有：lambda、map、filter、reduce
# gg=lambda x:x*2-1
# print(gg(5))

# # map:将序列中的元素全部传递给一个函数
# gglist=list(map(lambda x:x*x, range(1,10)))
# print(gglist)

# aa=list(filter(lambda r:r%3,range(10)))
# print(aa)

# list遍历筛选remove
    # fil=[".jpg",".JPG",".jpeg",".JPEG",".png",".PNG"]
    # for one in files:
    #     temp="".join(one)
    #     # print(temp)
    #     # if all(t.rfind(temp) for t in fil):
    #     # if all(t.index(temp)==-1 for t in fil):
    #     if all(t not in temp for t in fil):
    #         # print(one)
    #         files.remove(one)
