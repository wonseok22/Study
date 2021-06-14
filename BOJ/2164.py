import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    nums = deque([i for i in range(1,int(input())+1,1)])
    last = nums[0]
    while nums:
        last = nums[0]
        nums.popleft()
        if nums:
            last = nums[0]
            nums.append(nums.popleft())
    print(last)
