import sys
input = sys.stdin.readline

def solve(cnt, value):
    global answer

    if cnt == 11:
        answer = max(answer, value)

        return
    for i in range(11):
        if visited[i] or member[cnt][i] == 0:continue
        visited[i] = True
        solve(cnt + 1, value + member[cnt][i])
        visited[i] = False

for _ in range(int(input())):
    member = [list(map(int,input().split())) for i in range(11)]
    visited = [False for _ in range(11)]
    answer = 0
    solve(0, 0)
    print(answer)