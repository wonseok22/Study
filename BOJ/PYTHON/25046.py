from itertools import combinations
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
nums = list(range(0,N))
C = list()
for i in range(N+1): # 민우가 선택가능한 행의 모든 경우의 수
    for x in combinations(nums,i):
        C.append(x)
answer = -(float("inf"))
s = list() # 모든 열의 합
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += board[j][i]
    s.append(tmp)

for row_comb in C: #민우가 행을 선택하는 모든 경우에 대해
    ans_tmp = 0 # 정답 후보
    for i in range(N): # 모든 열에 대하여
        tmp = 0
        # 해당 열에서 (민우가 선택한 열의 합) 과 (해당 열의 합) - (민우가 선택한 열의 합)이
        # 더 작은 경우를 정답에 더해주면 됨
        for rows in row_comb:
            tmp += board[rows][i]
        ans_tmp += min(s[i]-tmp , tmp)
    answer = max(ans_tmp,answer)
print(answer)



