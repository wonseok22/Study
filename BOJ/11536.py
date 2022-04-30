import sys
input = sys.stdin.readline

N = int(input())
name = [input().strip() for _ in range(N)]
check = (name[0] < name[1])
for i in range(1,N-1):
    if check != (name[i] < name[i+1]):
        print("NEITHER")
        exit()
if check:
    print("INCREASING")
else:
    print("DECREASING")