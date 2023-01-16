import sys
input = sys.stdin.readline

N = int(input())
nums = [0 for _ in range(100001)]
for _ in range(N):
    num = int(float(input()) * 1000)
    nums[num] += 1
seven = 7
cnt = 0
while seven > 0:
    if nums[cnt] > 0:
        seven -= 1
        nums[cnt] -= 1
        print("{:.3f}".format(cnt / 1000))
    else:
        cnt += 1