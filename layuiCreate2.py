str='''
1 fid bigint 8 √ fid
2 listno varchar 30 单号
3 companyid int 4 门店id
4 fstate smallint 2 状态
5 sumqty decimal(18,2) 总数量
6 summount decimal(28,4) 总金额
7 unitid int 4 供应商id
8 fdate datetime 8 开单日期
9 indate datetime 8 交货日期
10 suminqty decimal(18,2) 到货数量
11 ordermount decimal(28,4) 订金金额
12 manager varchar 50 经办人
13 checker varchar 50 审核人
14 checkdate datetime 8 审核日期
15 notchecker varchar 50 反审核人
16 notcheckdate datetime 8 反审核日期
17 createtime datetime 8 创建时间
18 user varchar 50 制单人
19 lastupdater varchar 50 最后更新人
20 lastupdatetime datetime 8 最后更改时间
21 flag smallint 2 标志位
22 ischecklist bit 1 核对
23 checklister varchar 50 核对人
24 checklistdate datetime 8 核对日期
25 isdelete bit 1 已删除
26 canceler varchar 50 撤销人
27 canceldate datetime 8 撤销日期
28 remark varchar 200 备注
'''
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
            gg=index
            textone='"'+oneList[1]+'":"1",\n'
            text+=textone
    print(text)

    
change(str)