
N = int(input())
times = sorted([list(map(int,input().split())) for _ in range(N)], key = lambda x : (x[2],x[1]))

def findMax(times):
    ans = []
    for num,start,end in times:
        if ans:
            if ans[-1][2] <= start:
                ans.append([num,start,end])
        else:
            ans.append([num,start,end])
    return [x[0] for x in ans]
ans = findMax(times)
print(len(ans))
print([x[0] for x in ans])

