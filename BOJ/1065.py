N = int(input())
if N < 100:
    print(N)
elif N == 1000:
    print(144)
else:
    ans = 99
    for i in range(100,N+1):
        i = str(i)
        if int(i[1]) - int(i[0]) == int(i[2]) - int(i[1]):
            ans += 1
    print(ans)