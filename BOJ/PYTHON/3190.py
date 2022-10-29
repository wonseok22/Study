from collections import deque
import sys
# 상 하 좌 우
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    queue = deque([[0,0]])
    cnt = 0
    curr = 0
    i=0
    maps[0][0] = 2
    tale = deque([[0,0]])
    while queue:
        x,y = queue.popleft()
        if cnt == turn[i][0]:
            if turn[i][1] == "D":
                curr = (curr+1)%4
            else:
                curr = (curr-1)%4
            if i < len(turn)-1:
                i+=1
        ax = x + dx[curr]
        ay = y + dy[curr]
        cnt += 1
        if 0 <= ax < N and 0 <= ay < N:
            if maps[ax][ay] == 2:
                return cnt
            elif maps[ax][ay] == 0:
                a,b = tale.popleft()
                maps[a][b] = 0
                maps[ax][ay] = 2
                queue.append([ax,ay])
            elif maps[ax][ay] == 1:
                maps[ax][ay] = 2
                queue.append([ax,ay])
            tale.append([ax,ay])
        else:
            return cnt
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    maps = [[0]*N for _ in range(N)]
    for _ in range(K):
        a, b = map(int,sys.stdin.readline().split())
        maps[a-1][b-1] = 1
    L = int(sys.stdin.readline())
    turn = []
    for _ in range(L):
        a, b = sys.stdin.readline().split()
        turn.append([int(a),b])

    print(bfs())