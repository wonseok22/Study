from collections import deque
N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int,input().split())))
safe = []
#상 하 좌 우
dy = [0, 0 , -1, 1]
dx = [-1, 1, 0, 0]

def check_drown(i):
    for x in range(N):
        for y in range(N):
            if W[x][y] <= i:
                safe[x][y] = 1

def bfs(x,y):
    queue = [[x,y]]
    while queue:
        a, b = queue[0][0],queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<= x < N and 0 <= y < N and safe[x][y] == 0:
                safe[x][y] = 1
                queue.append([x,y])


if __name__ == "__main__":
    m = 0
    for i in range(1,101):
        cnt = 0
        safe = [[0] * N for _ in range(N)]
        check_drown(i)
        for x in range(N):
            for y in range(N):
                if safe[x][y] == 0:
                    safe[x][y] = 1
                    bfs(x,y)
                    cnt+=1

        m = max(m,cnt)
print(m)
