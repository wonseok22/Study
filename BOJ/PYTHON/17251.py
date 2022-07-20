N = int(input())-1
list = list(map(int,input().split()))
m = max(list)
maxl = []
for i in range(N+1):
    if list[i] == m:
        maxl.append(i)
