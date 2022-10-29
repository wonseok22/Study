
#상 하 좌 우
dx = [0 , 0 , -1 , 1]
dy = [-1 , 1 , 0 , 0]


def bfs(x,y):
    queue = [[x,y]]
    cnt = 1
    house[x][y] = 0
    while queue:
        ax = queue[0][0]
        ay = queue[0][1]
        del queue[0]
        for i in range(4):
            bx = ax + dy[i]
            by = ay + dx[i]
            if 0 <= bx < N and 0 <= by < N:
                if house[bx][by] == 1:
                    queue.append([bx,by])
                    cnt += 1
                    house[bx][by] = 0
    return cnt

if __name__ == "__main__":
    N = int(input())
    house = []
    answer = []
    for i in range(N):
        house.append(list(map(int,input())))
    for i in range(N):
        for j in range(N):
            if house[i][j] != 0:
                answer.append(bfs(i,j))
    print(len(answer))
    answer.sort()
    for i in answer:
        print(i)