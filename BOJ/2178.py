dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x,y):
    queue = [[x,y]]
    while queue:
        ax,ay = queue[0]
        del queue[0]
        for i in range(4):
            bx = ax + dy[i]
            by = ay + dx[i]
            if 0<=bx<N and 0<=by<M:
                if maze[bx][by] == '1':
                    maze[bx][by] = maze[ax][ay]+1
                    queue.append([bx,by])




if __name__ == "__main__":
    N,M = map(int,input().split())
    maze = []
    for _ in range(N):
        maze.append(list(input()))
    maze[0][0] = 1
    bfs(0,0)
    print(maze[N-1][M-1])