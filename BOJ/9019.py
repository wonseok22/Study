import sys
from collections import deque
input = sys.stdin.readline

def bfs(N,M):
    queue = deque()
    queue.append([N,""])
    c = [-1 for _ in range(10001)]
    c[N] = 0
    while queue:
        curr,command = queue.popleft()
        if curr == M:
            return command
        if c[(curr*2)%10000] == -1:
            queue.append([(curr*2)%10000,command+'D'])
            c[(curr*2)%10000] = 0

        if c[(curr-1)%10000] == -1:
            queue.append([(curr-1)%10000, command+'S'])
            c[(curr-1)%10000] = 0

        if c[curr % 1000 * 10 + curr // 1000] == -1:
            queue.append([curr % 1000 * 10 + curr // 1000,command+'L'])
            c[curr % 1000 * 10 + curr // 1000] = 0

        if c[curr % 10 * 1000 + curr // 10] == -1:
            queue.append([curr % 10 * 1000 + curr // 10,command+'R'])
            c[curr % 10 * 1000 + curr // 10] = 0


if __name__ == "__main__":
    for _ in range(int(input())):
        N,M = map(int,input().split())
        print(bfs(N,M))