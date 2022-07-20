import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
S = list(map(int,input().split()))
ans = 0
first = P.copy()

while [0,1,2]*(N//3) != P:
    tmp = [0]*N
    for i in range(N):
        tmp[S[i]] = P[i]
    if first == tmp:
        ans = -1
        break
    ans += 1
    P = tmp
print(ans)
