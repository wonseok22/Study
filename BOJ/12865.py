N,K = map(int,input().split())
T = []
for _ in range(N):
    T.append(list(map(int,input().split())))
visited = [0]*N
answer = 0
avg = sum(T[i][1] for i in range(N))/N

def dfs(W,V):
    global answer
    answer = max(answer,V)
    for i in range(N):
        if K >= W+T[i][0]:
            visited[i] = 1
            dfs(W+T[i][0],V+T[i][1])
            visited[i] = 0
dfs(0,0)
print(answer)

    
