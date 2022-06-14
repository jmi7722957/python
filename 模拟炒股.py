now_price=0.0000
now_number=0
now_total=0.0000
now_add_money=0.0000

def main():
    now_total=now_price*now_number
    now_price=
    print('now_price:'+now_price)
    print('now_number:'+now_number)
    print('now_total:'+now_total)
    print('now_add_money:'+now_add_money)

#买入
def add(price,number):
    now_total+=number*price

# 做T计算过程
'''
	#10
+3
$10
c30

	#6
+1
36/4=9
$9
c36

	#8
-1
c36-c8=c28
...3

之后全卖比较损失
...3
3x8=24
c28-24=c4

正常:
c30-24=c6

结论:做T有效

'''