if __name__ == "__main__":
    N,K = map(int,input().split())
    buyCnt = 0
    emptyGlass = 0
    if N <= K:
        print(0)
        exit()

    while True:
        buyCnt += 1
        emptyGlass = 0
        tmp = N
        while tmp != 0:
            if tmp%2 != 0:
                emptyGlass += 1
            tmp = tmp//2
        if emptyGlass<=K:
            break
        N+=1

    print(buyCnt-1)