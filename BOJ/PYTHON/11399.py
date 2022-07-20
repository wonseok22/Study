N = int(input().strip())
ans = 0
for i in sorted(list(map(int,input().split()))):
    ans += N * i
    N -= 1
print(ans)
