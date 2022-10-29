import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    flag = False
    S = input().strip()
    i = 0
    c = len(S)
    tmp = ''
    while S[i].isdigit() and i < c:
        tmp += S[i]
        i+=1
    stack = [int(tmp)]
    while i<c:
        tmp = ''
        if S[i] == 'S':
            i+=1
            if i >= c:
                break
            while S[i].isdigit():
                tmp += S[i]
                i+=1
                if i >= c:
                    break
            stack.append(stack.pop()-int(tmp))
        elif S[i] == 'M':
            i+=1
            if i >= c:
                break
            while S[i].isdigit():
                tmp += S[i]
                i += 1
                if i >= c:
                    break
            stack.append(stack.pop()*int(tmp))
        elif S[i] == 'U':
            i+=1
            if i >= c:
                break
            while S[i].isdigit():
                tmp += S[i]
                i += 1
                if i >= c:
                    break
            if int(stack[-1]) < 0:
                stack.append(-(abs(stack.pop())//int(tmp)))
            else:
                stack.append(stack.pop()//int(tmp))
        elif S[i] == 'P':
            i+=1
            if i >= c:
                break
            while S[i].isdigit():
                tmp += S[i]
                i += 1
                if i >= c:
                    break
            stack.append(stack.pop()+int(tmp))
        elif S[i] == 'C':
            print(stack[-1],end = ' ')
            flag = True
            i+=1
    if not flag:
        print('NO OUTPUT')