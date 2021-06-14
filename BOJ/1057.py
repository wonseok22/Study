
def bfs(start):
    queue = [start]
    cnt = 0 # 연결되어있는 컴퓨터 카운트
    while queue:
        X = queue[0] # popleft
        del queue[0]

        for L in link[X]:
            if checked[L] == 0 and L != 1: # 1번 제외하고 방문하지 않은 L번 컴퓨터와 연결되어있을 때
                checked[L] = 1 # visited 체크
                cnt += 1
                queue.append(L)
    return cnt



if __name__ == "__main__":
    N = int(input())
    K = int(input())
    link = [[] for _ in range(N+1)] # 컴퓨터들의 연결관계를 나타냄
    checked = [0 for _ in range(N+1)] # visited
    for _ in range(K):
        x,y = map(int,input().split())
        link[x].append(y)
        link[y].append(x)
    print(bfs(1)) 



