import sys
from collections import deque
input = sys.stdin.readline
S = deque(input().strip())
l = len(S)
cursor = l
for _ in range(int(input())):
    C = input().strip()
    if C == 'L':
        if cursor != 0:
            S.appendleft(S.pop())
            cursor -= 1
    elif C == 'D':
        if cursor != l:
            S.append(S.popleft())
            cursor += 1
    elif C == "B":
        if cursor != 0:
            S.pop()
            cursor -= 1
            l -= 1
    else:
        S.append(C[-1])
        cursor += 1
        l += 1
for _ in range(cursor):
    S.appendleft(S.pop())
print("".join(S))

