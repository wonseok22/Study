import sys

input = sys.stdin.readline

# 초기값 10 ** 9
# 방문 안하는 날


N, M = map(int,input().split())
max_coupon = (N // 5 + 1) * 2
dp = [[10 ** 9 for _ in range(max_coupon+1)] for _ in range(N+1)]
not_visit = [False for _ in range(N+1)]

if M > 0: # 방문 안하는 날 표시
    for i in list(map(int, input().split())):
        not_visit[i] = True

dp[0][0] = 0


for i in range(1, N+1): # 1일부터 마지막 날까지
    price = [10 ** 9 for _ in range(max_coupon+1)]
    if not_visit[i]: # 방문하지 못하는 날인 경우
        for num_coupon in range(max_coupon + 1):
            price[num_coupon] = min(
                dp[i - 1][num_coupon],
                dp[i - 3][num_coupon - 1] + 25000 if i > 2 else 10 ** 9,
                dp[i - 5][num_coupon - 2] + 37000 if i > 4 else 10 ** 9,
            )
    else: # 방문할 수 있는 날인 경우
        for num_coupon in range(max_coupon + 1):
            price[num_coupon] = min(
                dp[i - 1][num_coupon] + 10000,
                dp[i - 3][num_coupon - 1] + 25000 if i > 2 else 10 ** 9,
                dp[i - 5][num_coupon - 2] + 37000 if i > 4 else 10 ** 9,
                dp[i - 1][num_coupon + 3] if num_coupon < max_coupon - 2 else 10 ** 9
            )
    dp[i] = price

print(min(dp[i]))
