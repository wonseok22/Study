N = int(input())
nums = list(map(int,input().split()))
S = int(input())
sorted_index = 0
while S > 0 and sorted_index < N:
    # print("-------------------------")
    # print("S =",S, "sorted_index=",sorted_index)
    # 남은 정렬할 원소 개수
    remain_range = N - sorted_index
    # S랑 정렬할 개수 중 짧은거
    max_range = min(remain_range-1, S)
    # print("max_range = ",max_range)
    #탐색할 수 있는 범위
    search_nums = nums[sorted_index:sorted_index + max_range+1]

    # print("search_nums = ",search_nums)
    # 탐색할 수 있느 범위의 가장 큰 값의 인덱스 기준점 : sorted_index
    max_index = nums.index(max(search_nums))

    # print("max_index =",max_index)
    if max_index == sorted_index:
        sorted_index+=1
        continue
    S -= max_index-sorted_index
    nums = nums[:sorted_index] +  [nums[max_index]] + nums[sorted_index:max_index] + nums[max_index+1:]
    sorted_index += 1
    # print("nums = ", nums)
print(*nums,sep=" ")

