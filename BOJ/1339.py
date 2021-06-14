x = int(input())
num = []
for i in range(x):
    num.append(input())
weight = [0 for i in range(26)]
for i in range(len(num)):
    x = 0
    for j in range(len(num[i])-1,-1,-1):
        weight[ord(num[i][j])-ord('A')] += pow(10,x)
        x+=1
weight.sort(reverse = True)
ans=0
j = 9
for i in range(10):
    ans +=weight[i]*j
    j-=1
print(ans)
