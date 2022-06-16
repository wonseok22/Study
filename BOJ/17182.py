import sys
input = sys.stdin.readline


N,K = map(int,input().split())
time = [list(map(int,input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
visited[K] = 1
answer = float("inf")
for k in range(N):
    for i in range(N):
        for j in range(N):
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])

def find_min(curr, cost, cnt):
    global answer
    if N == cnt:
        answer = min(answer, cost)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            find_min(i, cost + time[curr][i], cnt+1)
            visited[i] = 0
find_min(K, 0, 1)
print(answer)