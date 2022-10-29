import sys
input = sys.stdin.readline

if __name__ =="__main__":
    N = int(input())
    A = list(map(int,input().split()))
    dp = [0 for _ in range(N)]
    dp[0] = 1
    for i in range(1,N):
        for j in range(i):
            if A[i] > A[j] and dp[j] >= dp[i]:
                dp[i] = dp[j]
        dp[i] += 1
    print(max(dp))
