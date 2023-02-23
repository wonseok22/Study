import sys
input = sys.stdin.readline

board = [list(map(int,input().split()))+[0] * 4 for _ in range(10)]
answer = [0] * 5
ans = 10 ** 9
for _ in range(4):
    board.append([0]*14)
def solve(start):
    global ans
    x,y = start
    if sum(answer) >= ans:
        return
    for i in range(x,10):
        for j in range(10):
            if i == x and j < y: continue
            if board[i][j] == 1: # 1이라면 색종이 붙이는 경우 혹인해야 함
                for offset in range(5): # 색종이 크기 1부터 5까지 네모 모양이 다 1인지 확인
                    check = True
                    for x_o in range(offset+1):
                        for y_o in range(offset+1):
                            if board[i + x_o][j + y_o] == 0:
                                check = False
                                break
                        if not check:
                            break
                    if not check: continue
                    if answer[offset] == 5: continue

                    for a in range(i, i+offset+1):
                        for b in range(j, j+offset+1):
                            board[a][b] = 0
                    answer[offset] += 1
                    solve([i,j+offset+1])
                    answer[offset] -= 1
                    for a in range(i, i+offset+1):
                        for b in range(j, j+offset+1):
                            board[a][b] = 1
                if board[i][j] == 1:
                    return
    ans = min(sum(answer), ans)

solve([0,0])
if ans == 10 ** 9:
    print(-1)
else:
    print(ans)



