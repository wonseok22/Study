import sys,time
input = sys.stdin.readline

N,K = map(int,input().split())
cost = [[0]*N for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    cost[a-1][b-1] = 1
start = time.time()
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] and cost[k][j]:
                cost[i][j] = 1
end = time.time()
print(f"{end - start:.5f} sec")
for _ in range(int(input())):
    i,j = map(int,input().split())
    if cost[i-1][j-1] == 1:
        print(-1)
    elif cost[j-1][i-1] == 1:
        print(1)
    else:
        print(0)

print(f"{end - start:.5f} sec")

