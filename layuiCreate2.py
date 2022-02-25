from fileinput import close


# 把旧的cols变成新的clos

from dataclasses import field
import re

newText="""
FID
ListNo
CompanyID
Fstate
SumQTY
SumMount
UnitID
Fdate
InDate
SumInQTY
OrderMount
Manager
Checker
CheckDate
NotChecker
NotCheckDate
CreateTime
Fuser
LastUpdater
LastUpdateTime
Flag
IsCheckList
CheckLister
CheckListDate
IsDelete
Canceler
CancelDate
Remark
ListNo
CompanyID
Fstate
SumQTY
SumMount
UnitID
Fdate
InDate
SumAbateMount
RealMount
Manager
Checker
CheckDate
NotChecker
NotCheckDate
CreateTime
Fuser
LastUpdater
LastUpdateTime
SumShipMount
SumOtherMount
Remark
Flag
IsCheckList
CheckLister
CheckListDate
IsRedList
IsDelete
OrderID
RedListTime
DeleteTime
MasterID
GoodsID
QTY
InQTY
Price
Color
Remark
CreateTime
Fuser
LastUpdater
LastUpdateTime
Findex
ListNo
CompanyID
Fstate
SumQTY
SumMount
UnitID
Fdate
OutDate
SumOutQTY
OrderMount
Manager
Checker
CheckDate
NotChecker
NotCheckDate
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
ClientName
MobileNo
IsCheckList
CheckLister
CheckListDate
IsDelete
QuotedPricer
QuotedPriceDate
DistStocker
DistStockDate
Flag
Canceler
CancelDate
FID
ListNo
CompanyID
Fstate
SumQTY
SumMount
UnitID
Fdate
RealMount
SumAbateMount
OrderMount
Manager
Checker
CheckDate
NotChecker
NotCheckDate
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
ClientName
MobileNo
Flag
IsCheckList
CheckLister
CheckListDate
IsRedList
IsDelete
OrderID
OrderDetailID
vipcardid
CarID
SumServiceMount
SumSBQTY
SumSBMount
RepairType
Repair
Mileage
ComeTime
GoTime
GetCarPerson
ChangeMileage
OtherMount
OtherMountType
RedListTime
DeleteTime
FID
MasterID
ServiceID
FHour
Price
Type
QTY
Discount
Disprice
integral
Remark
Repair
Saler
CreateTime
Fuser
LastUpdater
LastUpdateTime
Findex
FID
MasterID
GoodsID
QTY
CostPrice
DetailType
OrgiPrice
Price
Discount
Disprice
LessMount
Color
Remark
Wname
BatchNo
CreateTime
Fuser
LastUpdater
LastUpdateTime
integral
Findex
WarehouseID
OrderDetailID
FID
ListNo
CompanyID
IsStop
Fname
Type
BeginTime
EndTime
isonlyvip
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
IsDelete
Checker
CheckDate
NotChecker
NotCheckDate
ListNo
CompanyID
Fstate
SumMount
Fdate
Manager
Checker
CheckDate
NotChecker
NotCheckDate
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
IsCheckList
CheckLister
CheckListDate
IsDelete
Flag
IsRedList
RedListTime
DeleteTime
MasterID
GoodsID
QTY
Price
Color
Wname
WarehouseID
Remark
CreateTime
Fuser
LastUpdater
LastUpdateTime
Findex
BatchNo
WarehouseID
GoodsID
SQTY
Price
YLQTY
BatchNo
Color
Wname
StockMount
ShareMount
Flag
CreateTime
Fuser
LastUpdater
LastUpdateTime
WarehouseID
GoodsID
QTY
Wname
Color
DetailID
MasterID
Flag
CreateTime
Fuser
LastUpdater
LastUpdateTime
StockFlag
ListNo
CompanyID
UnitID
Mount
HadpayMount
ForeMount
AbateMount
vipcard_no
payintegral
vippaymount
vipcardmount
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
Flag
AddIntegral
IsRedList
RedListTime
DeleteTime
MasterID
ListID
Mount
SumMount
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
ListFlag
CompanyID
SumMount
HadpayMount
AbateMount
Fdate
UnitID
CreateTime
Fuser
LastUpdater
LastUpdateTime
Flag
Remark
IsFirst
SubjectID
AccountID
Abatemount
Fdate
UnitID
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
Flag
Manager
IsRedList
RedlistTime
FYear
FMonth
Fdate
BeginDate
EndDate
CreateTime
Fuser
LastUpdater
LastUpdateTime
IsBill
Remark
AccountID
Mount
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
Fdate
InCompanyID
InAccountID
Checker
CheckDate
NotChecker
NotCheckDate
Fdate
Fno
ReChecker
Manager
Super
CreateTime
Fuser
LastUpdater
LastUpdateTime
Remark
Fstate
Checker
CheckDate
NotChecker
NotCheckDate
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
                // {
                //     field: 'checker',
                //     width: 120,
                //     sort: true,
                //     title: '审核人',
                // },
                // {
                //     field: 'check_date',
                //     width: 120,
                //     sort: true,
                //     title: '审核日期',
                //
                // },
                // {
                //     field: 'notchecker',
                //     width: 120,
                //     sort: true,
                //     title: '反审核人',
                //
                // },
                // {
                //     field: 'notcheckdate',
                //     width: 120,
                //     sort: true,
                //     title: '反审核日期',
                //
                // },
                // {
                //     field: 'lastupdater',
                //     width: 120,
                //     sort: true,
                //     title: '最后更新人',
                //
                // },
                // {
                //     field: 'lastupdatetime',
                //     width: 120,
                //     sort: true,
                //     title: '最后更改时间',
                //
                // },
                // {
                //     field: 'flag',
                //     width: 120,
                //     sort: true,
                //     title: '标志位',
                //
                // },
                // {
                //     field: 'passnoid',
                //     width: 120,
                //     sort: true,
                //     title: '序列号',
                //
                // },
                // {
                //     field: 'step',
                //     width: 120,
                //     sort: true,
                //     title: '操作步骤',
                //
                // },
                // {
                //     field: 'priorstate',
                //     width: 120,
                //     sort: true,
                //     title: '上个状态',
                //
                // },
                // {
                //     field: 'priorcompanyid',
                //     width: 120,
                //     sort: true,
                //     title: '上个门店',
                //
                // },
                // {
                //     field: 'priorwarehouseid',
                //     width: 120,
                //     sort: true,
                //     title: '上个仓库',
                //
                // },
                // {
                //     field: 'priorbatchno',
                //     width: 120,
                //     sort: true,
                //     title: '上个批次号',
                //
                // },
                // {
                //     field: 'checklister',
                //     width: 120,
                //     sort: true,
                //     title: '核对人',
                // },
                // {
                //     field: 'checklistdate',
                //     width: 120,
                //     sort: true,
                //     title: '核对日期',
                //
                // },
                // {
                //     field: 'isdelete',
                //     width: 120,
                //     sort: true,
                //     title: '已删除',
                //
                // },
                // {
                //     field: 'batchno',
                //     width: 120,
                //     sort: true,
                //     title: '批次号',
                //
                // },
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