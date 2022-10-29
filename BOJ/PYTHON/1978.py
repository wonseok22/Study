import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    num = list(map(int,input().split()))
    ans = 0
    for i in num:
        flag = True
        if i == 1:
            continue
        for j in range(2,i):
            if i%j == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            ans += 1
    print(ans)