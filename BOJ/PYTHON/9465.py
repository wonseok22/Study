import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        board = [list(map(int,input().split())) for _ in range(2)]
        if N == 1:
            print(max(board[0][0], board[1][0]))
            continue
        board[0][1] += board[1][0]
        board[1][1] += board[0][0]
        for i in range(2,N):
            board[0][i] += max(board[1][i-1], board[1][i - 2])
            board[1][i] += max(board[0][i-1], board[0][i - 2])
        print(max(board[0][N-1],board[1][N-1]))