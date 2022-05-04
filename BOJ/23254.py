import sys
import heapq as hq
input = sys.stdin.readline


N, M = map(int,input().split())
score = list(map(int,input().split()))
up_score = list(map(int,input().split()))
time = 0
heap = []
answer = 0
for i in range(M):
    hq.heappush(heap,[-up_score[i],score[i]])
while 24*N > time and heap:
    b, a = hq.heappop(heap)
    if (100-a)//(-b) < 24*N - time:
        tmp = a + (-b * ((100-a)//(-b)))
        if tmp == 100:
            answer += 100
        else:
            hq.heappush(heap,[-(100 - tmp), tmp])
        time += (100-a)//(-b)
    else:
        answer += a + (24*N - time) * (-b)
        time += (24*N - time)
for b, a in heap:
    answer += a
print(answer)