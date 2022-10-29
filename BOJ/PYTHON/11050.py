import sys
input = sys.stdin.readline

def bino_coef(n, r):
    # 1.
    cache = [[0 for _ in range(r+1)] for _ in range(n+1)]

    # 2.
    for i in range(n+1):
        cache[i][0] = 1
    for i in range(r+1):
        cache[i][i] = 1

    # 3.
    for i in range(1, n+1):
        for j in range(1, r+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]

    return cache[n][r]
if __name__ == "__main__":
    n,k = map(int,input().split())
    print(bino_coef(n,k))