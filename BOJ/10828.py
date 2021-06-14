import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    q = deque([])
    for _ in range(int(input())):
        q.append(input().split())
    stack = []
    while q:
        x = q.popleft()
        if x[0] == 'push':
            stack.append(x[1])
        elif x[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif x[0] == 'size':
            print(len(stack))
        elif x[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif x[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)