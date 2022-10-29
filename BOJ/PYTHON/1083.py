N = int(input())
nums = list(map(int,input().split()))
S = int(input())
for _ in range(S):
    for i in range(N-1):
        if nums[i] < nums[i+1]:
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
            break
print(' '.join(map(str,nums)))
