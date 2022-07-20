
num , des = input().split()
des=int(des)
value = []
count = 0
for i in range(int(num)):
    value.append(int(input()))
while des>0:
    if value[i] <= des:
        des = des-value[i]
        count += 1
    else:
        i= i-1
print(count)
