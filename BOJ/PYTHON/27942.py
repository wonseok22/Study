import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

t = [N//2-1, N//2-1, N//2]
d = [N//2, N//2-1, N//2]
l = [N//2-1, N//2-1, N//2]
r = [N//2, N//2-1, N//2]
directions = ["U","D","L","R"]
answer = 0
answer_dir = ""
while True:
    dir = -1
    value = 0
    if 0 <= t[0] - 1:
        s = sum(board[t[0]-1][t[1]:t[2]+1])
        if  s > value:
            value = s
            dir = 0
    if d[0] + 1 < N:
        s = sum(board[d[0]+1][d[1]:d[2]+1])
        if  s > value:
            value = s
            dir = 1
    if 0 <= l[0] - 1:
        s = sum(board[j][l[0]-1] for j in range(l[1],l[2]+1))
        if  s > value:
            value = s
            dir = 2
    if r[0] + 1 < N:
        s = sum(board[j][r[0]+1] for j in range(r[1],r[2]+1))
        if  s > value:
            value = s
            dir = 3
    if dir == -1:
        break
    elif dir == 0:
        t[0] -= 1
        l[1] -= 1
        r[1] -= 1
    elif dir == 1:
        d[0] += 1
        l[2] += 1
        r[2] += 1
    elif dir == 2:
        l[0] -= 1
        t[1] -= 1
        d[1] -= 1
    else:
        r[0] += 1
        t[2] += 1
        d[2] += 1
    answer += value
    answer_dir += directions[dir]
print(answer)
print(answer_dir)


