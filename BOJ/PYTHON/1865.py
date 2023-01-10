import sys

input = sys.stdin.readline


def bellman_ford(start):
    distance[start] = 0
    # 전체 v - 1번의 라운드(round)를 반복
    for i in range(N):
        # 간선
        for curr,next,weight in edge:
            total = distance[curr] + weight
            if distance[next] > total:
                distance[next] = total
                if i == N-1:
                    return False
    return True


TC = int(input())
for _ in range(TC):
    N,M,W = map(int,input().split())
    edge = list()
    for _ in range(M):
        S,E,T = map(int,input().split())
        edge.append([S-1,E-1,T])
        edge.append([E-1,S-1,T])
    for _ in range(W):
        S,E,T = map(int,input().split())
        edge.append([S-1,E-1,-T])

    distance = [10e9 for _ in range(N)]
    if bellman_ford(0):
        print("NO")
    else:
        print("YES")

