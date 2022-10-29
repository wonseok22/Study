import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(start):
    b_queue = [[start]]
    w_queue = [drown[-1]]
    i=0
    while b_queue[-1] or w_queue[-1]:
        w_queue.append([])
        for k in w_queue[i]:
            x,y = k
            for z in range(4):
                ax = x + dx[z]
                ay = y + dy[z]
                if 0 <= ax < r and 0 <= ay < c:
                    if maps[ax][ay] == ".":
                        w_queue[-1].append([ax,ay])
                        maps[ax][ay] = "*"
        b_queue.append([])
        for k in b_queue[i]:
            x,y = k
            for z in range(4):
                ax = x + dx[z]
                ay = y + dy[z]
                if 0<= ax < r and 0 <= ay < c:
                    if maps[ax][ay] == "D":
                        print(i+1)
                        return
                    if maps[ax][ay] == ".":
                        b_queue[-1].append([ax,ay])
                        maps[ax][ay] = "S"
        '''for z in range(r):
            print(maps[z])

        print("\n")'''
        i+=1
    print("KAKTUS")


if __name__ == "__main__":
    r,c = map(int,sys.stdin.readline().split())
    maps = []
    for _ in range(r):
        maps.append(list(input()))
    drown = []
    drown.append([])
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "S":
                start = [i,j]
            if maps[i][j] == "*":
                drown[0].append([i,j])
    bfs(start)
