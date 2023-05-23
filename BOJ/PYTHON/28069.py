import sys
input = sys.stdin.readline


N,K = map(int,input().split())
while N % 3 == 0 :
    N = (N // 3) * 2
    K -= 1
# visited = [1000000 for _ in range(N+1)]
# q = deque()
# q.append(0)
# visited[0] = 0
# while q:
#     curr = q.popleft()
#     # print(q)
#     if curr == N:
#         if visited[curr] > K:
#             print("water")
#         else:
#             print("minigimbob")
#         exit()
#     if curr + 1 <= N and visited[curr+1] == float("inf"):
#         q.append(curr+1)
#         visited[curr+1] = visited[curr] + 1
#     if curr + curr//2 <= N and visited[curr+curr//2] == float("inf"):
#         q.append(curr+curr//2)
#         visited[curr+curr//2] = visited[curr] + 1

dp = [float("inf") for _ in range(N+1)]
dp[0] = 0
for i in range(N):
    if i+1 == N or i+i//2 == N:
        if dp[i] < K:
            print("minigimbob")
        else:
            print('water')
        break
    dp[i+1] = min(dp[i] + 1, dp[i+1])
    if i + i//2 < N: dp[i + i//2] = min(dp[i+i//2], dp[i] + 1)

