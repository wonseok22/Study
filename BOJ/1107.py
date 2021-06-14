import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    B = [str(i) for i in range(10)]
    b = list(input().split())
    b = list(set(B)-set(b))
    ans = abs(100-N)
    for num in range(1000001):
        num = str(num)
        for j in range(len(num)):
            if num[j] not in b:
                break
            elif j == len(num) - 1:
                ans = min(ans, abs(N - int(num)) + len(str(num)))
    print(ans)
