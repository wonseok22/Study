from collections import deque

if __name__ == "__main__":
    N,M = map(int,input().split())
    visited = [[-1,0] for _ in range(100001)]
    visited[N][0] = 0
    visited[N][1] = 1
    queue = deque()
    queue.append(N)
    answer = 1
    while queue:
        x = queue.popleft()
        for i in [x-1, x+1, x*2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] = visited[x][1]
                    queue.append(i)
                elif visited[i][0] == visited[x][0] + 1:
                    visited[i][1] += visited[x][1]
    print(visited[M][0])
    print(visited[M][1])