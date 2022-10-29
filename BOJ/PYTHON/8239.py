import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    ans = 0
    while True:
        if N % 5 == 0:
            ans += N // 5
            print(ans)
            break
        N -= 3
        ans += 1
        if N < 0:
            print(-1)
            break