if __name__ == "__main__":
    N,K = map(int,input().split())
    X = (K*(K+1))//2
    if N < X:
        print(-1)
    else:
        if (N-X)%K ==0:
            print(K-1)
        else:
            print(K)