

T = int(input())

def rotate(board):
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = board[r][c]
    for i in range(N):
        answer[i].append("".join(map(str,ret[i])))
    return ret

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    answer = [[] for _ in range(N)]
    for i in range(3):
        board = rotate(board)
    print("#{}".format(test_case))
    for i in range(N):
        print(' '.join(answer[i]))
