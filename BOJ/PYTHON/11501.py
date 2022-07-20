if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        nums = list(map(int,input().split()))
        curr = nums[-1]
        answer = 0
        for j in range(N-1,-1,-1):
            if nums[j] < curr:
                answer += curr-nums[j]
            else:
                curr = nums[j]
        print(answer)