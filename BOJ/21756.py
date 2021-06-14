import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = 0
    c = int(input())
    flag = True
    ans = 0
    if c == 1:
        print(1)
    else:
        while c>n:
            if flag:
                ans += 2
                n += 2
                flag = False
            else:
                ans += 2
                n += 4
                flag = True
        print(ans)