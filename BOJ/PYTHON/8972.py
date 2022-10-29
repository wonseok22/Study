import sys
input = sys.stdin.readline

R, C = map(int,input().split())
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1 ,-1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
arduino  = set()

board = [list(input().strip()) for _ in range(R)]

# 아두이노들의 좌표를 찾는다.
for i in range(R):
    for j in range(C):
        if board[i][j] == "I":
            robot = [i,j]
        elif board[i][j] == "R":
            arduino.add((i,j))

# 명령 실행
for cnt, command in enumerate(input().strip()):

    # 종수가 주어진 명령에 따라 아두이노를 이동함
    command = int(command)
    robot[0] += dx[command]
    robot[1] += dy[command]

    # 이동한 칸에 미친아두이노가 있는 경우 종료
    if (robot[0],robot[1]) in arduino:
        print("kraj",cnt+1)
        exit()

    move = set() # 이동한 미친 아두이노의 좌표
    crushed = set() # 충둘이 일어난 미친 아두이노의 좌표


    for x,y in arduino:
        m = [5, 201] # 최소 거리가 되는 방향을 저장

        # 8방향 중 거리가 최소가 되는 방햐 찾음
        for j in range(1,10):
            ax = x + dx[j]
            ay = y + dy[j]
            distance = abs(ax-robot[0]) + abs(ay-robot[1])
            if distance < m[1]:
                m = [j,distance]

        # 찾은 방향으로 이동
        x += dx[m[0]]
        y += dy[m[0]]
        if [x,y] == robot: # 종수의 아두이노를 잡은 경우
            print("kraj", cnt + 1)
            exit()
        elif (x,y) in move: # 미친 아두이노끼리 충돌한 경우
            crushed.add((x,y))
        else: # 정상적으로 이동할 수 있는 경우
            move.add((x,y))

    # 충돌이 일어난 미친 아두이노의 좌표를 이동한 미친 아두이노 좌표 집합에서 삭제
    for x,y in crushed:
        move.remove((x,y))
    arduino = move # 이동 완료한 아두이노의 좌표를 갱신해줌


# 출력을 위해 board를 새로 만들고 아두이노들의 좌표를 표시
board = [["." for _ in range(C)] for _ in range(R)]
for x,y in arduino:
    board[x][y] = "R"
board[robot[0]][robot[1]] = "I"
for i in range(R):
    print(''.join(board[i]))



