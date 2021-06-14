from itertools import combinations

N = int(input())
items = [i for i in range(N)]
W = []
for _ in range(N):
    W.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        W[i][j]+=W[j][i]
check = list(combinations(items,N//2))
answer = 10000

for x in check:
    first = 0
    sec = 0
    for val in list(combinations(x,2)):
        first += W[val[0]][val[1]]
    for val in list(combinations(set(items) - set(x),2)):
        sec += W[val[0]][val[1]]
    answer = min(abs(first-sec),answer)
print(answer)

