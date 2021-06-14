import sys
from collections import Counter
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = sorted([int(input()) for _ in range(N)])
    print(round(sum(nums)/N))
    print(nums[len(nums)//2])
    check = Counter(nums).most_common()
    if len(check) > 1:
        if check[0][1] == check[1][1]:
            print(check[1][0])
        else:
            print(check[0][0])
    else:
        print(check[0][0])
    print(max(nums)-min(nums))