import sys
input = sys.stdin.readline

N,K = map(int,input().split())
nums = list(map(int,input().split()))
print(sum(sorted([(nums[i+1] - nums[i]) for i in range(N-1)],reverse=True)[K-1:]))