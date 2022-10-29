import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
crain = sorted(list(map(int,input().split())), reverse=True)
box_n = int(input())
weight = deque(sorted(list(map(int,input().split())),reverse=True))
answer = 0
if weight[0] > crain[0]:
    print(-1)
    exit()
while weight:
    curr_crain = 0
    answer += 1
    for _ in range(box_n): # M
        w = weight.popleft()
        if curr_crain < N:  # 크레인을 다 사용하지 않은 경우
            if crain[curr_crain] >= w: # 크레인에 실을 수 있는 무게인 경우
                box_n -= 1
                curr_crain += 1
            else: # 크레인에 못 싣는 경우
                weight.append(w)
        else:
            weight.append(w)
    if answer >= 10000:
        break
print(answer)

