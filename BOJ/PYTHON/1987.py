import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    queue = deque([[start[0],start[1],alphabet[start[0]][start[1]]]])
    ans = 0
    while queue:
        x,y,check= queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < R and 0 <= ay < C and alphabet[ax][ay] not in check:
                queue.append([ax,ay,check+alphabet[ax][ay]])
                ans = max(ans,len(check)+1)
    return ans


if __name__ == "__main__":
    R,C = map(int,input().split())
    alphabet = [list(input().strip()) for _ in range(R)]
    print(bfs([0,0]))