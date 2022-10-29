N,S  = map(int,input().split())
nums = list(map(int,input().split()))
answer = 0
def bt(s, idx, cnt):
    global answer,S
    if s == S and cnt > 0:
        answer += 1
    for i in range(idx, N):
        bt(s+nums[i], i+1, cnt + 1)
bt(0,0,0)
print(answer)