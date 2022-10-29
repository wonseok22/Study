if __name__ == "__main__":
    N = int(input())
    balloon = list(map(int,input().split()))
    answer = []
    check = [0]*N
    idx = 0
    for i in range(N):
        answer.append(idx%N+1)
        check[idx%N] = 1
        cnt = balloon[idx%N]
        if i<N-1:
            while cnt:
                c = cnt
                if c > 0:
                    idx +=1
                else:
                    idx -=1
                if check[idx%N] == 0:
                    if cnt>0:
                        cnt -= 1
                    else:
                        cnt +=1

    for i in answer:
        print(i,end =" ")