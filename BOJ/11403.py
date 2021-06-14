import sys
from collections import deque
input = sys.stdin.readline

def find(start,board):
    queue = deque([start])
    check = [0 for _ in range(N)]
    #check[start] = 1
    while queue:
        x = queue.popleft()
        for i in range(N):
            if board[x][i] == 1 and check[i] == 0:
                #print(i,start)
                queue.append(i)
                check[i] = 1
    return check




if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        print(' '.join(map(str,find(i,board))))