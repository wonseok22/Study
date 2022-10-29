import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,K = map(int,input().split())
    st = input().strip()
    ans = [0]*N
    cnt = 0
    for idx,key in enumerate(st):
        if key == "H":
            ans[idx] = 1
    if N<=K:
        print(min(list(st).count('H'),list(st).count("P")))
    else:
        for idx,key in enumerate(st):
            if key == 'P':
                if idx > N-K-1:
                    for i in range(idx-K,len(st),1):
                        if ans[i] == 1:
                            ans[i] = 0
                            cnt += 1
                            break
                elif idx >= K:
                    for i in range(idx-K,idx+K+1,1):
                        if ans[i] == 1:
                            ans[i] = 0
                            cnt += 1
                            break
                elif idx < K:
                    for i in range(0,idx+K+1,1):
                        if ans[i] == 1:
                            ans[i] = 0
                            cnt += 1
                            break
        print(cnt)


