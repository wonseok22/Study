import sys
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(5)]
answer = set()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(n, y_cnt, visited, shape):
    global answer
    if n == 7 and y_cnt < 4:
        answer.add(''.join(sorted(shape)))
    for s in shape:
        x = int(s[-2])
        y = int(s[-1])
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < 5 and 0 <= ay < 5:
                if not visited[ax][ay]:
                    visited[ax][ay] = True
                    if board[ax][ay] == "Y":
                        if y_cnt < 3:
                            dfs(n+1, y_cnt+1,visited, shape+[str(ax)+str(ay)])
                    else:
                        dfs(n+1, y_cnt, visited, shape+[str(ax)+str(ay)])
                    visited[ax][ay] = False

for i in range(5):
    for j in range(5):
        visited = [[False for _ in range(5)] for _ in range(5)]
        visited[i][j] = True
        if board[i][j] == "Y": dfs(1, 1, visited,[str(i)+str(j)])
        else: dfs(1, 0, visited, [str(i)+str(j)])
print(len(answer))



