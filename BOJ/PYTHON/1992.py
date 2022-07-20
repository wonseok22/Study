import sys
input = sys.stdin.readline


def ans(x,y,n):

    check = board[x][y]
    for i in range(x,n+x):
        for j in range(y,n+y):
            if check != board[i][j]:
                a = ans(x,y,n//2)
                b = ans(x,y+n//2,n//2)
                c = ans(x+n//2,y,n//2)
                d = ans(x+n//2,y+n//2,n//2)
                return '('+a+b+c+d+')'

    if check == 0:
        return '0'
    else:
        return '1'







if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().strip())) for _ in range(N)]
    print(ans(0,0,N))