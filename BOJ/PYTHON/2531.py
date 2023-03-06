import sys
from collections import deque
input = sys.stdin.readline

N,D,K,C = map(int,input().split())
sushi = [int(input()) for _ in range(N)]
selected = deque()
answer = 0
for i in range(0,K):
    selected.append(sushi[i])
for i in range(N):
    check = len(set(selected))
    if C not in selected:
        check += 1
    answer = max(answer, check)
    selected.popleft()
    selected.append(sushi[(i+K) % N])
print(answer)