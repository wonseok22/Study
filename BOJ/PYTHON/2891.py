import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,S,R = map(int,input().split())
    B = list(map(int,input().split()))
    P = list(map(int,input().split()))
    ca = [0]*N
    for i in B:
        ca[i-1] -= 1
    for i in P:
        ca[i-1] += 1
    stack = []
    for i in ca:
        if stack:
            if i == -1:
                if stack[-1] == 1:
                    stack.pop()
                else:
                    stack.append(i)
            elif i == 1:
                if stack[-1] == -1:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(stack.count(-1))