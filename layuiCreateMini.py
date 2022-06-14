#根据数字字典数据,生成layui页面的clos或者data临时数据
import re

str='''
业务时间、门店、仓库、商品编号、商品名称、商品规格、调整前成本、调整后成本、调整人员
'''
# str=str.replace("√","")

def change(str):
    #去除换行
    list=str.split('、')
    text=""
    for index in range(len(list)):
        one=list[index].strip()
        if one!="":
            textone="""
                {
                    field:'name',
                    width:200,
                    sort:true,
                    title:'"""+one+"""'
                },"""
            text+=textone
    print(text)

change(str)
# change2(str)