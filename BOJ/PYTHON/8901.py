import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve(total):
    global answer
    if value[1] >= value[2]:
        total += value[1] * min(volume[1], volume[2])
        total += value[2] * min(volume[0], volume[2] - min(volume[1], volume[2]))
    else:
        total += value[2] * min(volume[0], volume[2])
        total += value[1] * min(volume[1], volume[2] - min(volume[0], volume[2]))
    answer = max(answer,total)
T = int(input())
for _ in range(T):
    answer = 0
    volume = list(map(int,input().split()))
    value = list(map(int,input().split()))
    cnt = 1
    solve(0)
    while volume[0] > 0 and volume[1] > 0:
        volume[0] -= 1
        volume[1] -= 1
        solve(value[0]*cnt)
        cnt += 1
    print(answer)