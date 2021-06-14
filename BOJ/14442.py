import sys
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,0]

def bfs(start):
    wall = 0
    queue = deque([start])
    x,y = start
    while queue:
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < n and 0 <= ay < m:
                if

if __name__ == "__main__":
    n,m,k = map(int,sys.stdin.readline().split())
    maps = []
    for _ in range(n):
        maps.append(list(map(int,sys.stdin.readline().split())))
    print(bfs([0,0]))
'''
    0000
    1110
    1000
    0000
    0111
    0000
'''