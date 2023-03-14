import sys
input = sys.stdin.readline

def select(n):
    return [((n+2)//2)*2, ((n+2)//2)*2 + 1]


def solve(cnt, value):
    global answer
    if value >= answer:
        return

    if cnt == 10 or cnt == 11:
        answer = min(value, answer)
        return

    for i in select(cnt):
        solve(i, value + times[unselect[cnt]][i])



times = [list(map(int,input().split())) for _ in range(12)]
unselect = [1,0,3,2,5,4,7,6,9,8,11,10]
answer = float("inf")
tmp = 0
for i in range(6):
    tmp += times[i*2][i*2+1]
solve(0, tmp)
solve(1, tmp)
print(answer)