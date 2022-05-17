import sys
input = sys.stdin.readline


#최단경로를 찾는 문제이기 때문에 우, 하 방햐응로만 가면 됨.
dx = [1,0]
dy = [0,1]
def dfs(x, y, route, sign):
    global min_answer, max_answer
    if x == N-1 and y == N-1:
        answer = eval(''.join(route))
        min_answer = min(answer,min_answer)
        max_answer = max(answer,max_answer)
        return
    for i in range(2):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < N and 0 <= ay < N and not visited[ax][ay]:
            visited[ax][ay] = True
            if sign:  # 부호가 나올 차례인 경우
                dfs(ax,ay, route + board[ax][ay],False)
            else: # 숫자가 나올 차례인 경우 ()로 묶음.
                dfs(ax,ay, "(" + route + board[ax][ay]+")", True)
            visited[ax][ay] = False


N = int(input())
max_answer = -float("inf")
min_answer = float("inf")
board = [list(input().strip().split()) for _ in range(N)]
visited = [[False for _ in range(N)]for _ in range(N)]
visited[0][0] = True
dfs(0,0,board[0][0], True)
print(max_answer,min_answer)

