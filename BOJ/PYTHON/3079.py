import sys
input = sys.stdin.readline

N,M = map(int,input().split())
T = [int(input()) for _ in range(N)]
start = min(T)
end = max(T) * M
while start < end :
    mid = (start + end)//2
    throughout = 0
    for t in T:
        throughout += mid // t
    if throughout >= M:
        end = mid
    else:
        start = mid+1
print(end)
