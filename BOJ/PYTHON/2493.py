import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tower = list(map(int,sys.stdin.readline().split()))
    stack = []
    answer = []
    for idx,value in enumerate(tower):
        while stack:
            if stack[-1][1] > value:
                answer.append(stack[-1][0]+1)
                break
            else:
                stack.pop()
        if not stack:
            answer.append(0)
        stack.append([idx,value])
    for value in answer:
        print(value,end = ' ')