from itertools import combinations

if __name__ == "__main__":
    n = int(input())
    M = int(input())
    nums = sorted(list(map(int,input().split())))
    cnt = 0
    front = 0
    rear = n-1
    while front<rear:
        if nums[front] + nums[rear] == M:
            cnt +=1
            front +=1
            rear -=1
        elif nums[front]+nums[rear] < M:
            front +=1
        else:
            rear -=1


    print(cnt)
