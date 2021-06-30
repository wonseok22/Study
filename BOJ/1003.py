import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    testCase = [int(input()) for _ in range(t)]
    dp0 = [0 for _ in range(41)]
    dp1 = [0 for _ in range(41)]
    dp0[0] = 1
    dp1[1] = 1
    for i in range(2, 41):
        dp0[i] = dp0[i - 1] + dp0[i - 2]
        dp1[i] = dp1[i - 1] + dp1[i - 2]
        
    for i in testCase:
        print(dp0[i],dp1[i])
