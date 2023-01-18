import sys
input = sys.stdin.readline


N,M = map(int,input().split())
switch = [int(input(),  2) for _ in range(N)]
K = int(input())
answer = 0
for i in range(N):
    count = 0
    for col in range(M):
        if switch[i] & (1 << col) == 0:
            count += 1

    if count > K or (K - count) % 2 == 1:
        continue
    ans_cnt = 0
    for j in range(N):
        if switch[i] ^ switch[j] == 0:
            ans_cnt += 1
    answer = max(ans_cnt, answer)
print(answer)


