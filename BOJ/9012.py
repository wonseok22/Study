import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        S = input().strip()
        stack = []
        for i in S:
            if stack:
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if stack:
            print('NO')
        else:
            print('YES')
