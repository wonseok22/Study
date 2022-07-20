from collections import deque

def leastCnt(nums,log):
    answer = 0
    sol = [0 for _ in range(nums)]
    log.sort()
    queue = deque(log)
    rear = -1
    front = 1
    sol[0] = queue.popleft()
    flag = 0
    while queue:
        X = queue.popleft()
        if flag == 0:
            flag = 1
            sol[rear] = X
            rear -= 1
        else:
            flag = 0
            sol[front] = X
            front +=1
    for i in range(len(sol)-1):
        if abs(sol[i+1]-sol[i]) > answer:
            answer = abs(sol[i+1]-sol[i])
    if abs(sol[-1]-sol[0]) > answer:
        answer = abs(sol[-1]-sol[0])
    return answer


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        nums = int(input())
        log = list(map(int,input().split()))
        print(leastCnt(nums,log))


        '''log.sort()
        answer = 0
        for i in range(2,nums):
            answer = max(answer, abs(log[i]-log[i-2]))
        print(answer)'''

