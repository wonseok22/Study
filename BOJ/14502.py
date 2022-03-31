from collections import deque
from itertools import permutations
import copy
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def cntzero(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                cnt += 1
    return cnt


def bfs(arr):
    queue = deque()
    for i in virus:
        queue.append(i)
    c = [[0 for _ in range(M)] for _ in range(N)]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < M:
                if c[ax][ay] == 0 and arr[ax][ay] == 0:
                    queue.append([ax,ay])
                    c[ax][ay] = 1
                    arr[ax][ay] = 2
    return cntzero(arr)

if __name__ == "__main__":
    answer = 0
    N,M = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(N)]
    l = []
    h = []
    virus = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                l.append([i,j])
            if maps[i][j] == 2:
                virus.append([i,j])
    for i in permutations(l,3):
        h.append(i)
    for x,y,z in h:
        m = copy.deepcopy(maps)
        m[x[0]][x[1]] = 1
        m[y[0]][y[1]] = 1
        m[z[0]][z[1]] = 1
        answer = max(answer,bfs(m))
    print(answer)