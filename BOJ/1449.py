N , L = input().split()
N = int(N)
L = int(L)
m = list(map(int,input().split()))
cnt = 0
i = 0
j = 0
m.sort()
while i<len(m):
    while j != len(m) and (L-1) >= m[j]-m[i]:
        j+=1
    i=j
    cnt+=1
print(cnt)
