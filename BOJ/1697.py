
def bfs(start):
    X = start
    if X == M:
        print(i)
        print(queue[-2].count(M))
        exit()
    print(X-1,X+1,2*X)
    if 0 < X <= 100000:
        if visited[X-1] == 0:
            queue[-1].append(X-1)
            visited[X-1] = 1
    if 0 <= X < 100000:
        if visited[X+1] == 0:
            queue[-1].append(X+1)
            visited[X+1] = 1
    if X*2 <= 100000:
        if visited[X*2] == 0:
            queue[-1].append(X*2)
            visited[X*2] = 1
    visited[M] = 0 

if __name__ == "__main__":
    N,M = map(int,input().split())
    visited = [0 for _ in range(100001)]
    queue = []
    queue.append([N])
    i=0
    while queue[-1]:
        queue.append([])
        print(queue[i])
        for z in queue[i]:
            bfs(z)
        i+=1