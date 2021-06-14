import sys
def bfs(start):
    queue = [start]
    check = [0]*(N+1)
    check[start] = 1
    cnt = 0
    while queue:
        X = queue[0]
        del queue[0]
        for Y in trust[X]:
            if check[Y] == 0:
                cnt+=1
                check[Y] = 1
                queue.append(Y)
    return cnt


if __name__ == "__main__":
    N,M = map(int,sys.stdin.readline().split())
    trust = [[] for _ in range(N+1)]
    answer = []
    for _ in range(M):
        x,y = map(int,sys.stdin.readline().split())
        trust[y].append(x)
    for start in range(1,N+1):
        if trust[start]:
            x = bfs(start)
            answer.append([start,x])
    m = max(answer,key = lambda x : x[1])
    #answer.sort( key = lambda x : x[1], reverse = True)
    for idx in answer:
        if idx[1] == m[1]:
            print(idx[0] ,end = ' ')

