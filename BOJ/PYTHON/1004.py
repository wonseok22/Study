import sys
input = sys.stdin.readline

for _ in range(int(input())):
    answer = 0
    x1,y1,x2,y2 = map(int,input().split())
    N = int(input())
    planet = [list(map(int,input().split())) for _ in range(N)]
    for x,y,r in planet:
        d1 = (((x1 - x) ** 2) + ((y1 - y) ** 2)) ** 0.5
        d2 = (((x2 - x) ** 2) + ((y2 - y) ** 2)) ** 0.5
        if d1 < r < d2 or d2 < r < d1: # 출발점 또는 도착점이 하나는 안에, 하나는 밖에 있는 경우
            answer += 1
    print(answer)