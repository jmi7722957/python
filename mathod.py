from decimal import Decimal, getcontext
from tokenize import Double


#循环处理拼接字符串(scnd代码转正常)
str='''
 1 def fun(num):
 2     count = int(num/2)
 3     while count>1:
 4         if(num%count == 0):
 5             print("%d的最大公约数是：%d" %(num,count))
 6             break
 7         count -= 1
 8     else:
 9         print("%d是素数" %num)
10 
11 n = int(input("请输入一个整数："))
12 fun(n)
'''
def change(str):
    strlist=str.split("\n")
    for li in strlist:
        print(li[2:])
change(str)


#股票计算
def stockGG():
    # inM=Decimal(input('购入'))
    inM=Decimal(9.355)
    # hand=int(input('多少手'))*100
    hand=int(3*100)
    outM=Decimal(input('卖出'))
    total=(outM-inM)*hand
    getcontext().prec=3
    print(total)
# stockGG()
    

#递归
def han(n,x,y,z):
    "将n层汉诺塔从x移动到z上"
    if n == 1:
        print(x,'-->',z)
    else:
        han(n-1,x,z,y)
        print(x,'-->',z)
        han(n-1,y,x,z)
n = int(input("input n:"))
# han(n,'X','Y','Z')

