import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([])
    queue.append(1)
    c = [-1 for _ in range(101)]
    c[1] = 0
    while queue:
        curr = queue.popleft()

        for i in range(1,7):
            movedPoint = curr + i
            if 0 < movedPoint <= 100:
                if c[movedPoint] == -1:
                    if H[movedPoint] != 0:
                        movedPoint = H[movedPoint]
                    if c[movedPoint] == -1:
                        queue.append(movedPoint)
                        c[movedPoint] = c[curr] + 1
    print(c[100])


if __name__ == "__main__":
    N,M = map(int,input().split())
    H = [0 for _ in range(101)]
    for i in range(N):
        x,y = map(int,input().split())
        H[x] = y
    for j in range(M):
        x,y = map(int,input().split())
        H[x] = y
    bfs()