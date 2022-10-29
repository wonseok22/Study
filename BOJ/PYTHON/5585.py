price = int(input())
exchange = 1000-price
count=0
while exchange > 0:
    if exchange >= 500:
        exchange = exchange-500
        count +=1
    elif exchange >= 100:
        exchange = exchange - 100
        count +=1
    elif exchange >= 50:
        exchange = exchange -50
        count +=1
    elif exchange >= 10:
        exchange = exchange - 10
        count += 1
    elif exchange >= 5:
        exchange = exchange - 5
        count += 1
    elif exchange >= 1:
        exchange = exchange - 1
        count += 1
print(count)
