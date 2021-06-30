import sys
input = sys.stdin.readline
b = 0
w = 0
def check(x,y,n):
    c = board[x][y]
    global b,w
    for i in range(x,x+n):
        for j in range(y,y+n):
            if c != board[i][j]:
                check(x,y,n//2)
                check(x+n//2,y,n//2)
                check(x,y+n//2,n//2)
                check(x+n//2,y+n//2,n//2)
                return
    if c == 1:
        b += 1
    else:
        w += 1

if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    check(0,0,N)
    print(w)
    print(b)