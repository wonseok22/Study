if __name__ == "__main__":
    S = list(input())
    stack = []
    answer = []
    checkOne = 0
    checkZero = 0
    for i in S:
        if stack:
            if i == stack[-1]:
                stack.append(i)
            else:
                if i == '0':
                    checkOne += 1
                else:
                    checkZero += 1
                stack = []
                stack.append(i)
        else:
            stack.append(i)
    if stack[-1] == '0':
        checkZero +=1
    else:
        checkOne +=1
    print(min(checkOne,checkZero))