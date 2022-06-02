import sys
input = sys.stdin.readline

def spring():
    global curr_tree
    tmp = []
    for _ in range(curr_tree):
        x,y,age = live_tree.pop()
        if board[x][y] >= age and age != 0:
            board[x][y] -= age
            age += 1
            tmp.append([x, y, age])
        else:
            curr_tree -= 1
            dead_tree.append([x, y, age])
    for x, y, age in tmp:
        live_tree.append([x,y,age])


def summer():
    while dead_tree:
        x,y,age = dead_tree.pop()
        board[x][y] += age//2


def autumn():
    global curr_tree
    tmp = []
    for _ in range(curr_tree):
        x,y,age = live_tree.pop()
        if age % 5 == 0:
            curr_tree -= 1
            for i in range(9):
                ax = x + dx[i]
                ay = y + dy[i]
                if 0 <= ax < N and 0 <= ay < N:
                    curr_tree += 1
                    if i == 4:
                        tmp.append([ax,ay,age])
                    else:
                        tmp.append([ax,ay,1])
        else:
            tmp.append([x,y,age])
    for x, y, age in tmp:
        live_tree.append([x,y,age])

def winter(N):
    for i in range(N):
        for j in range(N):
            board[i][j] += A[i][j]

dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]

N, curr_tree, K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
live_tree = []
for _ in range(curr_tree):
    x,y,age = map(int,input().split())
    x,y = x-1,y-1
    live_tree.append([x,y,age])
live_tree.sort(key = lambda x : x[2],reverse=True)
dead_tree = []
board = [[5 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    spring()
    summer()
    autumn()
    winter(N)

print(curr_tree)
