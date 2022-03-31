import sys
input = sys.stdin.readline

for _ in range(int(input())):
    dic = dict()
    nums = list(input().strip().replace(" ", "") for _ in range(int(input())))
    for i in nums:
        dic[i] = 1
    flag = True
    for i in nums:
        s = ""
        for j in i:
            s += j
            if s in dic and s != i:
                print("NO")
                flag = False
                break
        if not flag:
            break
    if flag:
        print("YES")


