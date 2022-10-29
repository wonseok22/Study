dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = [[x,y]]
    global wolf
    global sheep
    sheepcnt = 0
    wolfcnt = 0
    if maps[x][y] == "v":
        wolfcnt +=1
    elif maps[x][y] == "k":
        sheepcnt+=1
    maps[x][y] = "#"
    while queue:
        ax = queue[0][0]
        ay = queue[0][1]
        del queue[0]
        for i in range(4):
            bx = ax + dx[i]
            by = ay + dy[i]
            if 0 <= bx < N and 0 <= by < M:
                if maps[bx][by] == ".":
                    queue.append([bx,by])
                elif maps[bx][by] == "v":
                    queue.append([bx,by])
                    wolfcnt +=1
                elif maps[bx][by] == "k":
                    queue.append([bx,by])
                    sheepcnt +=1
                maps[bx][by] = "#"
    if wolfcnt >= sheepcnt:
        wolf += wolfcnt
    else:
        sheep += sheepcnt


if __name__ == "__main__":
    N,M = map(int,input().split())
    maps = []
    for i in range(N):
        maps.append(list(input()))
    sheep = 0
    wolf = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] != "#":
                bfs(i,j)
    print(sheep,wolf)