dy = [0,0,-1,1]
dx = [-1,1,0,0]
# 상, 하, 좌, 우



def bfs(j,k):
    queue = [[j,k]]
    while queue:
        a, b = queue[0][0],queue[0][1]
        field[a][b] = 0
        del queue[0]

        for i in range(4):
            j = a + dx[i]
            k = b + dy[i]
            if 0 <= j < M and 0 <= k < N and field[j][k] == 1:
                field[j][k] = 0
                queue.append([j,k])


if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        M,N,K = map(int,input().split())
        cnt = 0
        field = [[0]*N for _ in range(M)]
        for _ in range(K):
            j,k = map(int,input().split())
            field[j][k] = 1
        for j in range(M):
            for k in range(N):
                if field[j][k] == 1:
                    bfs(j,k)
                    cnt +=1
        print(cnt)


