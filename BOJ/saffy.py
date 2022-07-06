

T = int(input())



for test_case in range(1, T + 1):
    board = [list(map(int,input().split())) for _ in range(9)]
    answer = 1
    for i in range(9):
        col = set()
        answer &= len(set(board[i])) == 9
        for j in range(9):
            col.add(board[j][i])
        answer &= len(col) == 9
    for i in range(0,9,3):
        for j in range(0,9,3):
            check = set()
            for x in range(3):
                for y in range(3):
                    check.add(board[i+x][j+y])
            answer &= len(check) == 9
    print("#{}".format(test_case),answer)

