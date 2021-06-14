def bfs(start,end):
    queue = [start]
    cnt = 1
    while queue:
        X = queue[0]
        del queue[0]
        for L in link[X]:
            if L == end:
                return cnt
            if visit[L] == 0 and L != start:
                print(L,X)
                visit[L] = 1
                queue.append(L)
        cnt+=1
    return -1
"""        1
    2       3
4  5  6    7"""

if __name__ == "__main__":
    n = int(input())
    start,end = map(int,input().split())
    m = int(input())
    visit = [0 for _ in range(n+1)]
    link = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        link[x].append(y)
        link[y].append(x)
    print(bfs(start,end))