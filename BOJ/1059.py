import sys
input = sys.stdin.readline

L = int(input())
s = list(map(int,input().split()))
N = int(input())
answer = 0
if N in s:
    print(answer)
    exit()
s.sort()
for idx,i in enumerate(s):
    if i > N:
        while s[idx-1] < N:
            answer += (i-s[idx-1]-2)
            s[idx-1] += 1
            print(answer)
        print(answer)
        break

