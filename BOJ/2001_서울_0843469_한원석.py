

T = int(input())


for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for x in range(M):
                for y in range(M):
                    s += board[i + x][j + y]
            answer = max(s,answer)
    print("#{}".format(test_case), answer)