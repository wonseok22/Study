import sys
input = sys.stdin.readline
c1 = 0
c2 = 0
c3 = 0


def ans(x,y,n):
    global c1,c2,c3
    check = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != board[i][j]:
                ans(x, y, n // 3)
                ans(x, y + n // 3, n // 3)
                ans(x, y + (n * 2) // 3, n // 3)
                ans(x + n // 3, y, n // 3)
                ans(x + n // 3, y + n // 3, n // 3)
                ans(x + n // 3, y + (n * 2) // 3, n // 3)
                ans(x + (n * 2) // 3, y, n // 3)
                ans(x + (n * 2) // 3, y + n // 3, n // 3)
                ans(x + (n * 2) // 3, y + (n * 2) // 3, n // 3)
                return
    if check == -1:
        c1 += 1
    elif check == 0:
        c2 += 1
    else:
        c3 += 1


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    ans(0,0,N)
    print(c1)
    print(c2)
    print(c3)