import sys
input = sys.stdin.readline

# n 은 도시 갯수
# m 은 버스 갯수
n = int(input())
m = int(input())

# (n+1) by (n+1) 크기 Dp 테이블 생성
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 출발 도시, 도착 도시, 비용
for _ in range(m):
    get3,get4, cost = map(int,input().split())
    end = max(get3,get4)
    start = min(get3,get4)
    dp[end][start] = cost

# 구하고싶은 시작 to 도착 포인트
get1 , get2 = map(int,input().split())
getStart = min(get1,get2)
getEnd= max(get1,get2)
def MIN(arr):
    newArr=[]
    if sum(arr) == 0:
        return 0
    else:
        for elem in arr:
            if elem :
                newArr.append(elem)
    return min(newArr)

for e in range(getStart, getEnd+1):
    for s in range(getStart, e+1):
        if dp[e][s]:
            dp[e][s] = min(dp[e][s],dp[e][s] + MIN(dp[s]))
if getStart == getEnd:
    print(0)
else:
    print(MIN(dp[getEnd]))