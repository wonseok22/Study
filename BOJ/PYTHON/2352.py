# 해결하지 못함.
num = int(input())
x=input()
line = x.split()
new_line = []
cant = 1
cnt=0
for i in range(1, num+1):
    new_line.append((i,int(line[i-1]), abs(i-int(line[i-1]))))
new_line.sort(key = lambda x: (x[2],x[0]))
for i in range(len(new_line)):
    for j in range (i):
        if (new_line[j][0]-new_line[i][0])<0 and (new_line[j][1]-new_line[i][1])>0:
            cant = 0
            break
        elif (new_line[j][0]-new_line[i][0])>0 and (new_line[j][1]-new_line[i][1])<0:
            cant = 0
            break
    if cant == 1:
        cnt+=1
        cant=1
print(cnt)


