import sys
from collections import deque
input = sys.stdin.readline

dxdy = {
    "L" : [0,-1],
    "R" : [0, 1],
    "U" : [-1, 0],
    "D" : [1, 0]
}

def ward(R,C, check): # 와드 설치
    queue = deque()
    queue.append([R,C])
    board[R][C] = "X"
    answer[R][C] = "."
    while queue:
        x,y = queue.popleft()
        for key in dxdy:
            ax = x + dxdy[key][0]
            ay = y + dxdy[key][1]
            if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == check:
                board[ax][ay] = "X"
                answer[ax][ay] = "."
                queue.append([ax,ay])





N, M = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
answer = [["#" for _ in range(M)] for _ in range(N)]
R, C = map(int,input().split())
R, C = R-1, C-1
command = input().strip()

for c in command:
    if c == "W":
        if board[R][C] != "X": #이미 와드를 설치한 칸이 아닌 경우에만 와드 설치
            ward(R,C,board[R][C])
    else: # L,R,U,D의 경우
        R += dxdy[c][0]
        C += dxdy[c][1]


# 모든 명령이 종료된 후 현재 한별이의 위치와 사방의 시야는 확보되어야 함
answer[R][C] = "."
for key in dxdy:
    if 0 <= R+dxdy[key][0] < N and 0 <=  C+dxdy[key][1] < M:
        answer[R+dxdy[key][0]][C+dxdy[key][1]] = "."

#정답 출력
for i in answer:
    print(''.join(i))


