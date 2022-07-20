from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start, color):
    queue = deque()
    queue.append(start)
    visited = [[-1 for _ in range(6)] for _ in range(12)]
    visited[start[0]][start[1]] = 0
    check = [start] # 방문한 좌표들
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < 12 and 0 <= ay < 6 and visited[ax][ay] == -1 and board[ax][ay] == color: # 같은 색 좌표를 방문한 경우
                queue.append([ax,ay])
                check.append([ax,ay])
                visited[ax][ay] = 0
    if len(check) >= 4: # 방문한 좌표가 4개 이상이면 해당 좌표 빈공간으로 변경
        for x,y in check:
            board[x][y] = "."
        return True
    return False


board = [list(input()) for _ in range(12)]
flag = True
answer = 0
while flag:
    flag = False
    for i in range(11,-1,-1):
        for j in range(6):
            if board[i][j] != ".":
                flag |= bfs([i,j],board[i][j])
    if flag: # 연쇄가 하나라도 실행됐다면 빈 공간 삭제
        answer += 1
        for j in range(6):
            for i in range(10,-1,-1):
                for k in range(11, i, -1):
                    if board[i][j] != "." and board[k][j] == ".":
                        board[i][j],board[k][j] = board[k][j],board[i][j]
                        break
print(answer)

