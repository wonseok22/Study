import sys
input = sys.stdin.readline

d = [[-1,0], [0, 1], [1, 0], [0, -1]]


if __name__ == "__main__":
    N,M = map(int,input().split())
    R,C,D = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    while True:
        flag = False
        if board[R][C] == 0:    
            board[R][C] = 2
            answer += 1
        for i in range(4):
            ad = (D -i -1) % 4 
            ax = R + d[ad][0]
            ay = C + d[ad][1]
            if 0 <= ax < N and 0 <= ay < M and board[ax][ay] == 0:
                flag = True
                R,C,D = ax,ay,ad
                break
        # 네 방향에 청소할 공간이 없는 경우
        if not flag:
            # 한 칸 후진
            R -= d[D][0] 
            C -= d[D][1]

            # 보드 바깥으로 벗어난 경우
            if (0 > R or R >= N or 0 > C or C >= M):
                break
            
            # 뒤쪽이 벽인 경우
            if board[R][C] == 1:
                break
    print(answer)
            
