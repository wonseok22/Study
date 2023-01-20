import sys
input = sys.stdin.readline


N = int(input())
p = [list(map(int,input().split())) for _ in range(N)]
select = []
if N == 1:
    print(p[0][0])
    exit()
s,e = p[0]
ns, ne = p[1]
if e < ns:
    select.append(e)
elif s > ne:
    select.append(s)
else
cnt = 1
stress = 0
while cnt < N:
    s,e = p[cnt]
    if select[-1] < s:
        select.append(s)
    elif select[-1] > e:
        select.append(e)
    else:
        select.append(select[-1])
    cnt += 1

print(stress)
for i in select:
    print(i)




