dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    queue = [start]
    cnt = 1
    ch = maps[start[0]][start[1]]
    maps[start[0]][start[1]] = 0
    while queue:
        x,y = queue[0]
        del queue[0]
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0<=ax<M and 0<=ay<N:
                if ch == maps[ax][ay]:
                    queue.append([ax,ay])
                    maps[ax][ay] = 0
                    cnt +=1
    return cnt

if __name__ == "__main__":
    N,M = map(int,input().split())
    maps = []
    wC = 0
    bC = 0
    for _ in range(M):
        maps.append(list(input()))
    for i in range(M):
        for j in range(N):
            if maps[i][j] != 0:
                if maps[i][j] == "W":
                    cnt = bfs([i,j])
                    wC += cnt*cnt
                else:
                    cnt = bfs([i,j])
                    bC += cnt*cnt

    print(wC,bC)
