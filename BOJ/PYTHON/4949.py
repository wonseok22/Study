import sys
#input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        S = input()
        if S == '.':
            break
        stack = []
        for i in S:
            if i == ')':
                if stack:
                   if stack[-1] == '(':
                       stack.pop()
                   else:
                       stack.append(i)
                else:
                    stack.append(i)
            elif i == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            elif i == '[' or i == '(':
                stack.append(i)
        if stack:
            print('no')
        else:
            print('yes')
