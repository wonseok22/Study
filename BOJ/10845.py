import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    q = deque([])
    for _ in range(int(input())):
        q.append(input().split())
    stack = deque([])
    while q:
        x = q.popleft()
        if x[0] == 'push_front':
            stack = deque(x[1:]) + stack
        elif x[0] == 'push_back':
            stack += x[1:]
        elif x[0] == 'pop_front':
            if stack:
                print(stack.popleft())
            else:
                print(-1)
        elif x[0] == 'pop_back':
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
        elif x[0] == 'front':
            if stack:
                print(stack[0])

            else:
                print(-1)
        elif x[0] == 'back':
            if stack:
                print(stack[-1])
            else:
                print(-1)