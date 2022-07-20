T = int(input())
M = m = s = 0
if T%10 != 0:
    print(-1)
else:
    M = m = s = 0
    M = T // 300
    m = (T % 300) // 60
    s = (T % 300) % 60 // 10
    print(M, m, s)
