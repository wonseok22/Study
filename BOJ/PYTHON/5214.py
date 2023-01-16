import sys
from collections import deque
input = sys.stdin.readline


N,K,M = map(int,input().split())
hyper_tube = []
graph = [[]for _ in range(N+1)]
for i in range(M):
    hyper_tube.append(list(map(int,input().split())))
    for station in hyper_tube[i]:
        graph[station].append(i)
visited = [0 for _ in range(N+1)]
q = deque()
q.append(1)
visited[1] = 1
while q:
    curr = q.popleft()
    # 모든 하이퍼튜브를 확인
    if curr == N:
        print(visited[curr])
        exit()
    for ht in graph[curr]:
        for next in hyper_tube[ht]:
            if visited[next] == 0:
                visited[next] = visited[curr] + 1
                q.append(next)
        hyper_tube[ht] = []
print(-1)