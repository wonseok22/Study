
if __name__ == "__main__":
    N,M = map(int,input().split())
    loc = list(map(int,input().split()))
    queue = []
    for i in range(1,N+1):
        queue.append(i)

    curr1 = 0
    curr2 = 0
    cnt = 0
    while loc:
        find = loc[0]
        if queue.index(find) < len(queue)-queue.index(find):
            while queue[curr1] != find:
                curr += 1
                cnt += 1
            if curr1 >= N-1:
                curr1 = 0
        while queue[curr2] != find:
            curr2 -= 1
            cnt2 += 1
        #print(cnt1,cnt2)
        del loc[0]
        del queue[curr1]
        N-=1
        #print(queue,cnt)
    print(cnt)

