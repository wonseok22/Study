import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
left = 1
right = 0
answer = 0
def bfs(weight):  # 무게(wieght)를 기준으로 BFS탐색
    queue = deque()
    queue.append(f) #시작점은 무조건 f
    visited = [0 for _ in range(N+1)]
    visited[f] = 0
    while queue:
        x = queue.popleft()
        for i,w in graph[x]:
            if w >= weight and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    if visited[t] != 0: return True  #갈 수 있을 때
    return False # 못 갈 때

for _ in range(M): #양방향 그래프 구현
    a,b,c = map(int,input().split())
    right = max(right,c) # 이분 탐색의 끝 점을 정의하기 위함
    graph[a].append([b,c])
    graph[b].append([a,c])
f,t = map(int,input().split())  # 출발점, 도착점

while left <= right:
    mid = (left+right)//2
    if bfs(mid): # 출발점에서 도착점까지 무게 mid를 옮길 수 있는 경우
        answer = mid
        left = mid+1
    else: # 못 옮기는 경우
        right = mid -1
print(answer)