N = int(input())
K  = []
ans= 0
for i in range(N):
    K.append(int(input()))
for i in range(N-1,0,-1):
    if K[i]<= K[i-1]:
        ans +=K[i-1]-K[i]+1
        K[i-1] = K[i] - 1
print(ans)