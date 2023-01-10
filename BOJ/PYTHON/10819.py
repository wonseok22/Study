import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int,input().split())),reverse=True)
new_arr = [0] * N
print("arr= ",arr)
for i in range(N//2):
    new_arr[i*2] = arr[i]
    new_arr[i*2+1] = arr[-(i+1)]
    print(arr[i], arr[-(i+1)])
print(new_arr)
