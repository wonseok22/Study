value, brand = map(int,input().split())
pay_set = []
pay_single = []
for i in range(brand):
    x,y=map(int,input().split())
    pay_set.append(x)
    pay_single.append(y)
pay_set.sort()
pay_single.sort()
pay = 0
if pay_set[0] < pay_single[0]*6:
    while value >= 6:
        value -= 6
        pay+=pay_set[0]
    while value > 0:
        if value*pay_single[0]<pay_set[0]:
            value -= 1
            pay += pay_single[0]
        else:
            value=0
            pay+=pay_set[0]
else:
    pay = pay_single[0]*value
print(pay)
