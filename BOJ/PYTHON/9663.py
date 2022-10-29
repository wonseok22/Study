import sys
input = sys.stdin.readline


N = int(input())
answer = 0
board = [0]*N

def promising(row):
    for i in range(row):
        if board[i] == board[row] or abs(board[row]-board[i]) == abs(row-i):
            return False
    return True

def nQueen(row):
    global answer,board
    if row == N: # N개의 퀸을 다 놓은 경우 정답 카운트
        answer += 1
    else:
        for i in range(N): # N개의 col에 대해
            board[row] = i
            if promising(row):
                nQueen(row+1)

nQueen(0)
print(answer)

