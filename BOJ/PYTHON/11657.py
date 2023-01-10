
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
edge = list()
distance = [10e9 for _ in range(N)]
start = 0
for _ in range(M):
    a,b,c = map(int,input().split())
    edge.append([a-1,b-1,c])
distance[start] = 0
# 전체 v - 1번의 라운드(round)를 반복
for i in range(N):
    # 간선
    for curr,next,weight in edge:
        total = distance[curr] + weight
        if distance[curr] != 10e9 and distance[next] > total:
            distance[next] = total
            if i == N-1:
                print(-1)
                exit()
for i in distance[1:]:
    if i == 10e9:print(-1)
    else:print(i)


