import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    tip = sorted([int(input()) for _ in range(N)],reverse=True)
    ans = 0
    for idx,tips in enumerate(tip):
        if tips - idx <= 0:
            break
        ans += tips - idx
    print(ans)