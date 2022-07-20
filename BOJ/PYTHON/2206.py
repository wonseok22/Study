from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


if __name__ == "__main__":
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1

    while queue:
        x, y, c = queue.popleft()
        if x==N-1 and y==M-1:
            print(visited[x][y][c])
            exit()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<= ax < N and 0 <= ay < M:
                if graph[ax][ay] == 0 and visited[ax][ay][c] == 0:
                    queue.append((ax, ay, c))
                    visited[ax][ay][c] = visited[x][y][c] + 1
                if graph[ax][ay] == 1 and c == 0:
                    queue.append((ax, ay, c + 1))
                    visited[ax][ay][c + 1] = visited[x][y][c] + 1
    print(-1)
