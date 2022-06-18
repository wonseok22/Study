N = int(input())
nums = [False for _ in range(10**6+1)]
answer = 1
for i in range(2,N+1):
    if nums[i]: continue
    t = 1
    for j in range(i,N+1,i):
        nums[j] = True
        tmp = j
        cnt = 0
        while tmp > 1 and tmp % i == 0:
            tmp //= i
            cnt += 1
        t = max(t,cnt)
    for _ in range(t):
        answer = (answer*i) % 987654321
print(answer)

