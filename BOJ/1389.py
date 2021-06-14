import sys
from collections import deque
def bfs(start):
    cnt = 0
    w = [0 for _ in range(n+1)]
    queue = deque([start])
    while queue:
        p = queue.popleft()
        for k in relations[p]:
            if w[k] == 0 and k != start:
                queue.append(k)
                w[k] = w[p]+1
    answer[start-1] = sum(w)

if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())

    relations = [[] for _ in range(n+1)]
    for _ in range(m):
        A,B = map(int,sys.stdin.readline().split())
        relations[A].append(B)
        relations[B].append(A)
    answer = [0 for _ in range(n)]
    for i in range(1,n+1):
        bfs(i)
    print(answer.index(min(answer))+1)