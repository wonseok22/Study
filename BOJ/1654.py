import sys
input = sys.stdin.readline

k,n = map(int,input().split())
l = [int(input().strip()) for _ in range(k)]
i = 1
j = max(l)
while i <= j:
    mid = (i+j)//2
    cnt = sum([key // mid for key in l])
    if cnt >= n:
        i = mid + 1
        ans = mid
    elif cnt < n:
        j = mid - 1
print(ans)