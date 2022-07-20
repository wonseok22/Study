N = int(input())
nums = sorted([list(map(int,input().split())) for _ in range(N)], key = lambda x : x[2], reverse=True)
cnt = [0] * (N+1)
answer = 0
i = 0
while answer < 3:
    if cnt[nums[i][0]] < 2:
        cnt[nums[i][0]] += 1
        print(nums[i][0],nums[i][1])
        answer += 1
    i += 1