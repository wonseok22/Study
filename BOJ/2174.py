
dx = [-1, 0, 1, 0]
dy = [0, 1, 0,-1]
A,B = map(int,input().split())
N,M = map(int,input().split())
command = []
robot = dict()
board = [[0]*A for _ in range(B)]
for i in range(1,N+1):
    x,y,d = input().split()
    if d == "N":
        d = 0
    elif d == "E":
        d = 1
    elif d == "S":
        d = 2
    else:
        d = 3
    board[(B-int(y))][int(x)-1] = 1
    robot[i] = [(B-int(y)),int(x)-1,d]
for _ in range(M):
    x,y,d = input().split()
    command.append([int(x),y,int(d)])
for R, C, repeat in command:
    for _ in range(repeat):
        if C == "F":
            curr_x, curr_y, direction = robot[R]
            next_x = curr_x + dx[direction]
            next_y = curr_y + dy[direction]
            if not (0 <= next_x < B and 0 <= next_y < A):
                print("Robot",R,"crashes into the wall")
                exit()
            elif board[next_x][next_y] == 1:
                for i in robot:
                    if next_x == robot[i][0] and next_y == robot[i][1]:
                        print("Robot",R,"crashes into robot",i)
                        exit()
            else:
                board[curr_x][curr_y] = 0
                board[next_x][next_y] = 1
                robot[R][0] = next_x
                robot[R][1] = next_y
        elif C == "L":
            robot[R][2] = (robot[R][2]-1)%4
        else:
            robot[R][2] = (robot[R][2]+1)%4
print("OK")