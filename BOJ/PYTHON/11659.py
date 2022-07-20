import sys
input = sys.stdin.readline

if __name__ =="__main__":
    N,M = map(int,input().split())
    nums = list(map(int,input().split()))
    sums = [0 for _ in range(N)]
    for i in range(N):
        if i != 0:
            sums[i] = sums[i-1] + nums[i]
        else:
            sums[i] = nums[i]
    for _ in range(M):
        i,j = map(int,input().split())
        if i == 1:
            print(sums[j-1])
         else:
            print(sums[j-1]-sums[i-2])
