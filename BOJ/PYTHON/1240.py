import sys
from collections import deque

def bfs(start,end):

    queue = deque([start])
    length = [-1 for _ in range(n+1)]
    length[start] = 0
    while queue:
        s = queue.popleft()
        for e,w in tree[s]:
            if length[e] == -1:
                queue.append(e)
                length[e] = max(length[s] + w,length[e])
    return length[end]


if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        s,e,w = map(int,input().split())
        tree[s].append([e,w])
        tree[e].append([s,w])
    for _ in range(m):
        start,end = map(int,input().split())
        print(bfs(start,end))