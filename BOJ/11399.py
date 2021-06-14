
y=int(input())
x = list(map(int, input().split()))
x.sort()
i_sum = 0
min_sum = 0

for i in range(y):
    min_sum += (i_sum + x[i])  # 3
    i_sum += x[i]  # 4

print(min_sum)