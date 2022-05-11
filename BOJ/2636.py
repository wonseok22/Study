import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
prev = 0

def bfs():
    global answer,prev
    answer += 1
    queue = deque()
    queue.append([0,0])
    visited = [[False for _ in range(M)] for _ in range(N)] # 방문여부확인
    visited[0][0] = True
    melting_list = []
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < M and not visited[ax][ay]:
                if board[ax][ay] == 1:
                    melting_list.append([ax,ay])
                if board[ax][ay] == 0:
                    queue.append([ax,ay])
                visited[ax][ay] = True
    if melting_list: # 이번 탐색에서 녹일 치즈가 있다면
        for x,y in melting_list: # 치즈를 녹이는 과정
            board[x][y] = 0
        return len(melting_list)
    else: # 이번 탐색에서 녹일 치즈가 없다면 직전 bfs 탐색에서 모든 치즈가 녹은 것, 따라서 prev값과 answer-1 출력
        print(answer-1)
        print(prev)
        return False

while True : # 모든 치즈가 녹을 때까지 실행
    prev = bfs() # prev는 이전 bfs에서 녹인 치즈의 수
    if not prev:
        break
