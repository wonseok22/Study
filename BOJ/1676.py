import sys
input = sys.stdin.readline

if __name__ == "__main__":
    ans = 1
    for i in range(1,int(input())+1,1):
        ans *= i
    start = 10
    cnt = 0
    while True:
        if ans%start != 0:
            break
        cnt +=1
        start *= 10
    print (cnt)
    '''
    ans = str(ans)
    start = len(ans)-1
    cnt = 0
    while True:
        if ans[start] != '0':
            break
        start -= 1
        cnt += 1
    print(cnt)
    '''