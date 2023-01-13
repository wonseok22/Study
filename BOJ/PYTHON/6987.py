import sys
from itertools import combinations
input = sys.stdin.readline

def solve(game,cnt):
    if answer[game] == 1:
        return

    if cnt == 15:
        if score[game] == [0] * 18:
            answer[game] = 1
        return

    curr_home, curr_away = comb[cnt]
    for home, away in [[2,0], [1,1], [0,2]]:
        if score[game][curr_home*3+home] > 0 and score[game][curr_away*3 + away] > 0:
            score[game][curr_home * 3 + home] -= 1
            score[game][curr_away * 3 + away] -= 1
            solve(game, cnt+1)
            score[game][curr_home * 3 + home] += 1
            score[game][curr_away * 3 + away] += 1



score = [list(map(int,input().split())) for _ in range(4)]
answer = [0 for _ in range(4)]
comb = list(combinations(list(range(6)),2))
for i in range(4):
    solve(i,0)
print(*answer, sep=" ")