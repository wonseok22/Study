for _ in range(int(input())):
    x, y = map(int,input().split())
    curr = 0
    ans = 0
    cnt = 1
    while curr < y-x:
        ans += 1
        curr += cnt
        if ans % 2 == 0:
            cnt += 1
    print(ans)
