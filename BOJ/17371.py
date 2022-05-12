import sys
input = sys.stdin.readline

def distance(h1,h2):
    return (h1[0]-h2[0])**2 + (h1[1] - h2[1])**2

N = int(input())
loc = [tuple(map(int,input().split())) for _ in range(N)]
answer = [float("inf"),(0,0)]
for h1 in loc: # 가장 가까운 편의시설과 집 위치 후보
    m = [0,(0,0)]
    for h2 in loc: # 가장 먼 편의시실 후보
        if h1 != h2: # 같은 좌표는 제외
            d = distance(h1,h2)
            if d > m[0]: # 가장 먼 거리의 편의시설을 찾음
                m = [d, h2]
    if answer[0] > m[0]: # 가자 먼 거리의 편의시설의 거리들 중 최소가 정답
        answer = [m[0],h1]

print(answer[1][0], answer[1][1])
