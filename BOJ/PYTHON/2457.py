import sys
input = sys.stdin.readline
N = int(input())
flowers = []
target = [61,331]
for _ in range(N):
    start_m, start_d, end_m, end_d = map(int,input().split())
    flowers.append([(start_m-1)*30 + start_d, (end_m-1)*30+end_d])
flowers.sort(key = lambda x : (x[0],x[1]))
idx = 0
answer = 0
m = 0
print(flowers)
while True:
    for i in range(idx,N):
        print(i)
        if target[0] >= flowers[idx][0]:
            m = max(m,flowers[idx][1])
        else:
            answer += 1
            target[0] = m
            idx = i+1
            break
    if target[0] >= target[1] or idx == N-1:
        break
print(answer)

