import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().strip())
    nums = [int(input().strip()) for _ in range(n)]
    lst = [i for i in range(2,n+1)]
    stack = [1]
    answer = ['+']
    while lst or stack[-1] == nums[0]:
        if stack[-1] != nums[0]:
            stack.append(lst[0])
            del lst[0]
             answer.append('+')
        else:
            del nums[0]
            stack.pop()
            answer.append('-')
    for i in answer:
        print(i)