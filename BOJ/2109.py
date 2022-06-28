import sys
import heapq as hq
input = sys.stdin.readline


N = int(input())
uni = []
answer = []
curr_uni = 0
for _ in range(N):
    p,d = map(int,input().split())
    uni.append([p,d])
for p,d in sorted(uni, key=lambda x : x[1]): # 강연 데드라인을 기준, 오름차순 정렬
    hq.heappush(answer,p)
    curr_uni += 1 # 갈 수 있는 강연의 후보 개수 증가
    if curr_uni > d: # 갈 수 있는 강연의 후보 개수가 데드라인을 넘긴 경우
        hq.heappop(answer) # 가장 돈을 적게 주는 강연을 뺌
        curr_uni -= 1
print(sum(answer))

