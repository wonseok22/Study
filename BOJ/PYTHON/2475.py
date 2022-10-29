nums = list(map(int,input().split()))
ans = 0
for i in nums:
    ans += i*i
print(ans%10)