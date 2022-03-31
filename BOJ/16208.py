import sys
input = sys.stdin.readline

N = int(input())
length = sorted(list(map(int,input().split())))
answer = 0
first = sum(length)
for i in length:
    first -= i
    cost = first*i
    answer += cost
print(answer)

player = ((player+1) % 2) + 1
0 1 0 1
if player == 1:
        player = 2
    else:
        player = 1


