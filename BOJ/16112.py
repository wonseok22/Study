import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n,k = map(int,input().split())
    exp = sorted(list(map(int,input().split())))
    ans = 0
    idx = 0
    if n == 1:
        print(ans)
        exit()
    for i in range(n):
        ans += exp[i] * idx
        if idx<k:
            idx += 1
    print(ans)

