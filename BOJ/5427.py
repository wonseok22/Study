import sys
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():

    c = [[-1]*w for _ in range(h)]
    m = 0
    c[s_queue[0][0][0]][s_queue[0][0][1]] = 0
    while f_queue[-1] or s_queue[-1]:
        f_queue.append([])
        s_queue.append([])
        for z in f_queue[m]:
            x,y = z
            for i in range(4):
                ax = x + dx[i]
                ay = y + dy[i]
                if 0 <= ax < h and 0 <= ay < w:
                    if building[ax][ay] == ".":
                        building[ax][ay] = "*"
                        f_queue[-1].append([ax,ay])
        for z in s_queue[m]:
            x,y = z
            for i in range(4):
                ax = x + dx[i]
                ay = y + dy[i]
                if 0 <= ax < h and 0 <= ay < w:
                    if building[ax][ay] == "." and c[ax][ay] == -1:
                        c[ax][ay] = c[x][y] + 1
                        building[ax][ay] = "@"
                        s_queue[-1].append([ax,ay])
                else:
                    return c[x][y]+1

        m+=1
    return -1

if __name__ == "__main__":
    testCase = int(sys.stdin.readline())
    for _ in range(testCase):
        w,h = map(int,input().split())
        building = []
        s_queue = [[]]
        f_queue = [[]]
        for _ in range(h):
            building.append(list(input()))
        for i in range(h):
            for j in range(w):
                if building[i][j] == "@":
                    s_queue[0].append([i,j])
                if building[i][j] == "*":
                    f_queue[0].append([i,j])
        answer = bfs()

        if answer == -1:
            print("IMPOSSIBLE")
        else:
            print(answer)
