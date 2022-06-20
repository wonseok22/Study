dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,dir,cnt):
    if x == tx and y == ty :
        print(visited[x][y])


N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
fx,fy,fd = map(int,input().split())
tx,ty,td = map(int,input().split())
visited[fx][fy] = 0


