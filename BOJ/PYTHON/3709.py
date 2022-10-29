import sys
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(int(input())):
    N, R = map(int,input().split())
    mirror = {tuple(map(int,input().split())) for _ in range(R)}
    visited = set()
    x,y = map(int,input().split())

    # 방향 설정 0 -> 3으로 상, 우, 하, 좌의 순서.
    if x == N+1:
        d = 0
    elif x == 0:
        d = 2
    elif y == N+1:
        d = 3
    else:
        d = 1

    # 다음 진행할는 방향을 검사
    while True:
        x += dx[d]
        y += dy[d]
        # 보드 밖으로 벗어났다면
        if not (0 < x <= N and 0 < y <= N):
            print(x,y)
            break
        # 이미 방문한 거울을 같은 방향에서 또다시 방문한다면 보드 밖을 벗어나지 못함
        if (x,y) in mirror and (x,y,d) in visited:
            print(0,0)
            break
        # 처음 거울을 방문했다면면
        elf (x,y) in mirror:
            visited.add((x, y, d))
            d = (d+1)%4

