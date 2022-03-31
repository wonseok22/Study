import sys
import math
input = sys.stdin.readline



if __name__ == "__main__":
    N = int(input())
    dp = [0,1]
    for i in range(2,N+1):
        M = 10000000
        j = 1
        while j**2 <= i:
            M = min(M,dp[i-(j**2)])
            j+=1
        dp.append(M+1)
    print(dp[N])

