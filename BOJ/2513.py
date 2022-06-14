import sys
from collections import deque
input = sys.stdin.readline


N, K, S = map(int,input().split())
left = []
right = []
for _ in range(N):
    x,y = map(int,input().split())
    if x > S:
        left.append([abs(S-x),y])
    elif x < S:
        right.append([abs(S-x),y])
left = deque(sorted(left,key = lambda x : x[0], reverse=True))
right = deque(sorted(right,key = lambda x : x[0], reverse=True))
curr = 0
answer = 0
while left:
    answer += (left[0][0] * 2)
    while left and left[0][1] <= K-curr: # 전부 실을 수 있는 경우
        d, h =left.popleft()
        curr += h
    if left: # 일부만 실을 수 있는 경우
        left[0][1] -= K-curr
        curr = 0
curr = 0
while right:
    answer += (right[0][0] * 2)
    while right and right[0][1] <= K - curr:  # 전부 실을 수 있는 경우
        d, h = right.popleft()
        curr += h
    if right:  # 일부만 실을 수 있는 경우
        right[0][1] -= K - curr
        curr = 0
print(answer)