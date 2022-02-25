#根据数字字典数据,生成layui页面的clos或者data临时数据
import re

str='''
1	FID	int	4	fid
2	Fno	varchar	30	编号
3	Fname	varchar	50	名称
4	Flag	smallint	2	标志位
5	Type	smallint	2	类型0 配件1 整车
6	Remark	varchar	200	备注
7	IsZero	bit		默认价为零
8	IsSelectUnit	bit		选择往来单位
9	Type	smallint		出入库类型0 进货1 销售2 售后3 其他入库4 其他出库
10	CreateTime	datetime	8	创建时间
11	Fuser	varchar	50	制单人
12	LastUpdater	varchar	50	最后更新人
13	LastUpdateTime	datetime	8	最后更改时间
'''
str=str.replace("√","")

def change(str):
    #去除换行
    list=str.split('\n')
    text=""
    for index in range(len(list)):
        one=list[index].strip()
        if one!="":
            list[index]=one
            oneList=one.split('\t')
            #解析成list
            #print(oneList[1])
            title=oneList[4: ]
            # print(len(oneList))
            if len(oneList)<5:
                title=oneList[3: ]
            #字段名
            titleStr="".join(title)
            # print(titleStr)
            #字段key
            keyName=oneList[1]
            # print(keyName)

            reg=r"\d\s{0,1}([\u4e00-\u9fa5]{1,8})?"
            reg2=r"(\d)\s{0,1}[\u4e00-\u9fa5]{1,8}?"
            reg3=r"[\u4e00-\u9fa5]{1,8}"
            rule=re.compile(reg)
            rule2=re.compile(reg2)
            rule3=re.compile(reg3)
            #if,else匹配的类型名
            typeList=rule.findall(titleStr)
            #if,else匹配的类型id
            numList=rule2.findall(titleStr)
            #获取真正字段名
            titleList=rule3.findall(titleStr)
            if len(titleList)>0:
                titleStr=titleList[0]
            # print(typeList)
            # print(numList)

            templet=""
            elseList=""
            if len(typeList)>0:
                for index in range(1,len(typeList)):
                    elseList+="""else if(item."""+keyName+"""=="""+numList[index]+"""){
                                t='"""+typeList[index]+"""';
                            }"""

                    templet="""templet:function(item){
                            var t="-";
                            if(item.ftate==0){
                                t='"""+typeList[0]+"""';
                            }"""+elseList+"""
                            return t;
                        }"""
                    

            textone="""
                {
                    field:'"""+keyName+"""',
                    width:120,
                    sort:true,
                    title:'"""+titleStr+"""',"""+templet+"""
                },"""
            text+=textone
    print(text)

# def change2(str):
#     #去除换行
#     list=str.split('\n')
#     text=""
#     for index in range(len(list)):
#         one=list[index].strip()
#         if one!="":
#             list[index]=one
#             oneList=one.split(' ')
#             #解析成list
#             gg=index
#             textone='"'+oneList[1]+'":"1",\n'
#             text+=textone
#     print(text)
    
change(str)
# change2(str)