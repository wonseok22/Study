import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    length = [-1 for _ in range(V+1)]
    length[start] = 0
    while queue:
        s = queue.popleft()
        for k,m in rel[s]:
            if length[k] == -1:
                queue.append(k)
                length[k] = max(length[s]+m,length[k])
    z = max(length)
    return [length.index(z),z]

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    rel = [[] for _ in range(V+1)]
    for _ in range(V):
        check = list(map(int,sys.stdin.readline().split()))
        i = 1
        while check[i] != -1:
            rel[check[0]].append([check[i],check[i+1]])
            i+=2
    answer = 0
    print(bfs(bfs(1)[0])[1])