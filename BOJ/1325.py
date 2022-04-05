import sys
from collections import deque
def bfs(start):
    queue = deque()
    queue.append(start)
    check = [0]*(N+1)
    check[start] = 1
    while queue:
        X = queue.popleft()
        for Y in trust[X]:
            if check[Y] == 0:
                check[Y] = 1
                queue.append(Y)
    return sum(check)


if __name__ == "__main__":
    N,M = map(int,sys.stdin.readline().split())
    trust = [[] for _ in range(N+1)]
    answer = []
    m = 0
    for _ in range(M):
        x,y = map(int,sys.stdin.readline().split())
        trust[y].append(x)
    for start in range(1,N+1):
        x = bfs(start)
        if m < x:
            answer = [start]
            m = x
        elif m == x:
            answer.append(start)
    print(' '.join(map(str,answer)))


