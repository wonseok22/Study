import sys
input = sys.stdin.readline

inorder = input().strip()

stack = list()
for s in inorder:
    if s.isalpha():
        print(s,end="")
    elif s == "(":
        stack.append(s)
    elif s == ")":
        while True:
            if stack[-1] == "(":
                stack.pop()
                break
            print(stack.pop(),end="")
    elif s == "*" or s == "/":
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(),end="")
        stack.append(s)
    else:
        while stack and stack[-1] != "(":
            print(stack.pop(),end="")
        stack.append(s)
while stack:
    print(stack.pop(),end="")

