import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global ans
    board[x][y] = 1
    ans += 1
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == 0:
            dfs(ax,ay)

N, M, K = map(int,input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
answer = []
for _ in range(K):
    r1,c1,r2,c2 = map(int,input().split())
    for i in range(r1,r2):
        for j in range(c1,c2):
            board[(N-j-1)%N][i] = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            ans = 0
            dfs(i,j)
            answer.append(ans)
print(len(answer))
print(' '.join(map(str,sorted(answer))))


