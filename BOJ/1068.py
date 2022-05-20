import sys
from collections import deque
input = sys.stdin.readline
answer = 0
N = int(input())
tree = [[] for _ in range(N)]
visited = [False for _ in range(N)]
root = 0
for idx, parent in enumerate(list(map(int,input().split()))):
    if parent == -1:
        root = idx
    else:
        tree[parent].append(idx)
delete = int(input())
if delete == root:
    print(0)
    exit()
visited[root] = True
visited[delete] = True
queue = deque()
queue.append(root)
while queue:
    flag = True
    x = queue.popleft()
    if tree[x]:
        for i in tree[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                flag = False
        if flag:
            answer += 1
    else:
        answer += 1
print(answer)
