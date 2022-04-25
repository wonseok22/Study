N = int(input())
arr = list(map(int,input().split()))
for i in range(N-1,0,-1):
    if arr[i] < arr[i-1]:
        arr[i],arr[i-1] = arr[i-1],arr[i]
        arr = arr[:i+1] + sorted(arr[i+1:])
        print(' '.join(map(str,arr)))
        exit()
print(-1)