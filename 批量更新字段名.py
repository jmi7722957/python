from fileinput import close


# 把旧的cols变成新的clos
#建立一个自定义字典,根据字典把奇奇怪怪的字段名按照既定规则更正

from dataclasses import field
import re

newText="""
FID
ListNo
CompanyID
Fstate
SumQTY
SumMount
Fuser
LastUpdater
LastUpdateTime
Flag
IsCheckList
CheckLister
CheckListDate
"""

cols='''
                {
                    field: 'listno',
                    width: 120,
                    sort: true,
                    title: '单号',

                },
                {
                    field: 'ischecklist',
                    width: 120,
                    sort: true,
                    title: '核对',
                },
                {
                    field: 'fdate',
                    width: 120,
                    sort: true,
                    title: '开单日期',
                },
                {
                    field: 'companyid',
                    width: 120,
                    sort: true,
                    title: '门店',

                },
                {
                    field: 'warehosueid',
                    width: 120,
                    sort: true,
                    title: '仓库',
                },
                {
                    field: 'user',
                    width: 120,
                    sort: true,
                    title: '制单人',
                },
                {
                    field: 'createtime',
                    width: 120,
                    sort: true,
                    title: '创建时间',

                },
                {
                    field: 'sumqty',
                    width: 120,
                    sort: true,
                    title: '总数量',

                },
                {
                    field: 'summount',
                    width: 120,
                    sort: true,
                    title: '总金额',

                },
                {
                    field: 'price',
                    width: 120,
                    sort: true,
                    title: '价格',

                },
                {
                    field: 'remark',
                    width: 120,
                    sort: true,
                    title: '备注',
                },
                {
                    field: 'fstate',
                    width: 120,
                    sort: true,
                    title: '状态',
                    templet: function(item) {
                        var t = "-";
                        if (item.ftate == 0) {
                            t = '草稿';
                        }else if (item.fstate==1) {
                            t = '审核';
                        }else if (item.fstate==4) {
                            t = '作废';
                        }
                        return t;
                    }

                },
'''
# 新的需要匹配的字段数组
newList=newText.strip().split('\n')
def main(cols):
    # 获取最新的字段list
    # print(newList)

    # reg=r"field:'(.+){1,10}',"
    # rule=re.compile(reg)
    # list=rule.findall(cols)
    # 匹配替换
    gg=re.sub(r"field:\s?'(.+){1,10}',", change, cols)
    print(gg)

    # for index in range(len(list)):
    #     print(list[index])

#对每个匹配的字段进行单独处理再放回去
def change(one):
    field=one.group(1)
    # print(field)
    if field.strip()=='':
        return "field:'',"
    else:
        # 循环跟新的字段list匹配,替换
        for newF in newList:
            if newF.lower().find(field.lower())>=0:
                field=newF
                break
        return "field:'"+field+"',"

main(cols)