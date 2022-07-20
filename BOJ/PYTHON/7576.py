dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(start,i):
    x = start[0]
    y = start[1]
    for k in range(4):
        ax = x + dy[k]
        ay = y + dx[k]
        if 0<=ax<M and 0<=ay<N:
            if tomato[ax][ay] == 0:
                queue[-1].append([ax,ay])
                tomato[ax][ay] = 1

if __name__ == "__main__":
    N,M = map(int,input().split())
    tomato = []*M
    queue = []
    queue.append([])
    for i in range(M):
        tomato.append(list(map(int,input().split())))
    for i in range(M):
        for j in range(N):
            if tomato[i][j] == 1:
                queue[0].append([i,j])
    i=0
    while queue[i]:
        queue.append([])
        for start in queue[i]:
            bfs(start,i)
        i+=1
    for j in range(M):
        if 0 in tomato[j]:
            print(-1)
            exit()
    print(i-1)