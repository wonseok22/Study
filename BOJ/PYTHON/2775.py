import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        n = int(input())
        ans = [i for i in range(1,n+1)]
        for _ in range(k):
            for j in range(1,n):
                ans[j] += ans[j-1]
        print(ans[n-1])