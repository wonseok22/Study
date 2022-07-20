from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])
answer = float("inf")
for check in combinations(chicken, M):
    S = 0
    for h in house:
        S += min([abs(h[0] - i[0]) + abs(h[1] - i[1]) for i in check])
    answer = min(S, answer)
print(answer)
