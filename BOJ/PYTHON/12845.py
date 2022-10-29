import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    L = list(map(int,input().split()))
    ans = 0
    m = 0
    for i in L:
        if i >= m:
            m = i
        ans += i
    ans += m*(n-2)
    print(ans)
