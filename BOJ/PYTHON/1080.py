import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,M = map(int,input().split())
    A = [list(map(int,input().strip())) for _ in range(N)]
    B = [list(map(int,input().strip())) for _ in range(N)]
    ans = 0
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                for x in range(i,i+3):
                   for y in range(j,j+3):
                       A[x][y] = abs(A[x][y]-1)
                ans += 1
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                print(-1)
                exit()
    print(ans)