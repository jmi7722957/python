import re


str='''
2 companyid int 4 门店id
3 fdate datetime 8 日期
4 fno varchar 30 凭证号
5 rechecker varchar 50 复核
6 manager varchar 50 记账
7 super varchar 50 会计主管
8 createtime datetime 8 创建时间
9 lastupdater varchar 50 最后更新人
10 lastupdatetime datetime 8 最后更改时间
11 remark varchar 200 备注
12 fstate smallint 2 状态0 草稿1 审核2 作废
13 checker varchar 50 审核人
14 checkdate datetime 8 审核日期
15 notchecker varchar 50 反审核人
16 notcheckdate datetime 8 反审核日期
17 user varchar 50 操作人
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
            oneList=one.split(' ')
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
            #字段名list
            typeList=rule.findall(titleStr)
            #字段值list
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
                    title:'"""+titleStr+"""',
                    """+templet+"""
                },"""
            text+=textone
    print(text)

def change2(str):
    #去除换行
    list=str.split('\n')
    text=""
    for index in range(len(list)):
        one=list[index].strip()
        if one!="":
            list[index]=one
            oneList=one.split(' ')
            #解析成list
            gg=index
            textone='"'+oneList[1]+'":"1",\n'
            text+=textone
    print(text)
    
change(str)
change2(str)