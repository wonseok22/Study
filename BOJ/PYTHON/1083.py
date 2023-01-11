N = int(input())
nums = list(map(int,input().split()))
S = int(input())
sorted_index = 0
while True:
    if sorted_index == N-1 or S == 0:
        break
    max_value = nums.index(max(nums[:min(len(nums),S)+1]))
    print(nums[max_value],end= " ")
    nums[max_value] = 0
    sorted_index += 1
    S -= max_value-sorted_index
    print("s = ", S)
    print(nums)



for i in nums:
    if i != 0:
        print(i, end=" ")
