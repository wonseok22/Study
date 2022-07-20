import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    price = sorted([int(input()) for _ in range(N)],reverse=True)
    ans = 0
    for i in range(len(price)):
        if i % 3 != 2:
            ans += price[i]
    print(ans)
