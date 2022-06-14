from decimal import Decimal, getcontext
from tokenize import Double


#循环处理拼接字符串(scnd代码转正常)
str='''
                    <div style="text-align: center;padding: 20px;">
                        <img class="layui-col-md3 layui-block" src="../src/img/no-data.png" />
                        <div class="layui-col-md3 layui-block" style="color: #4f7aa3;">当前没有投诉记录</div>
                    </div>
'''
def change(str):
    strlist=str.split("\n")
    for li in strlist:
        print(li[2:])
# change(str)


#html转js string
str='''
<div style="text-align: center;padding: 20px;">
    <img class="layui-col-md3 layui-block" src="../src/img/no-data.png" />
    <div class="layui-col-md3 layui-block" style="color: #4f7aa3;">当前没有投诉记录</div>
</div>
<div class="follow-record follow-record_div{{ item.id}}">
    <div class="items layui-panel">
        <div class="fu-right">
            <div><span class="type">投诉门店：{{ item.storeName}}</span></div>
            <div><span class="time">状态：{{ item.status}}</span></div>
            <div><span class="time">投诉业务员：{{ item.employeeName}}</span></div>
            <div><span class="time">投诉时间：{{ item.createTm}}</span></div>
            <div><span class="time">投诉内容：{{ item.content}}</span></div>
            <div><span class="time">回复人：{{ item.operator}}</span></div>
            <div><span class="time">回复时间：{{ item.operationTm}}</span></div>
            <div><span class="time">回复内容：{{ item.result}}</span></div>
        </div>
    </div>
</div>
'''
def change(str):
    strlist=str.split("\n")
    for li in strlist:
        print("'"+li+"'+")
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

