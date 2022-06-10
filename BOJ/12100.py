import sys,copy
from collections import deque
input = sys.stdin.readline

def up(board):
    global answer
    queue = queue.
    is_concat = True
    for j in range(N):
        for i in range(1,N):
            queue.append()
    print("up")
    print(*board,sep='\n')
    return board

def down(board):
    global answer
    for j in range(N):
        for i in range(N-1,-1,-1):
            if board[i][j] != 0:

    print("down")
    print(*board,sep='\n')
    return board

def left(board):
    global answer
    for i in range(N):
        for j in range(1,N):
            if board[i][j] != 0:
                for k in range(j-1,-1,-1):
                    if board[i][k] != 0:
                        if board[i][j] == board[i][k]:
                            board[i][k] *= 2
                            board[i][j] = 0
                            answer = max(answer, board[i][k])
                            break
                        else:
                            board[]
    print("left")
    print(*board,sep='\n')
    return board

def right(board):
    global answer
    for i in range(N):
        for j in range(N-1,-1,-1):
            if board[i][j] != 0:
                for k in range(j+1,N):
                    if board[i][j] == board[i][k]:
                        board[i][k] *= 2
                        board[i][j] = 0
                        answer = max(answer, board[i][k])
                        break
    print("right")
    print(*board,sep='\n')
    return board


def bt(board,count):
    if count == 5:
        return
    bt(up(copy.deepcopy(board)), count + 1)
    bt(down(copy.deepcopy(board)), count + 1)
    bt(left(copy.deepcopy(board)), count + 1)
    bt(right(copy.deepcopy(board)), count + 1)

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
bt(board,0)
print(answer)


