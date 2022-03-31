from itertools import combinations

M = int(input())
stone = list(map(int,input().split()))
K = int(input())
N = sum(stone)
total = len(list(combinations(stone, K)))
same_color = 0
for s in stone:
    same_color += len(list(combinations(, K)))

print(same_color/total)