import sys
from collections import Counter
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    size = sorted(list(map(int,input().split())), reverse = True)
    ans = 0
    check = Counter(size)
    for i in check:
        if ans < check[i]:
            ans = check[i]
    print(ans)