if __name__ == "__main__":
    N = int(input())
    length = list(map(int,input().split()))
    weight = list(map(int,input().split()))
    cost = 0
    curr = 0
    if weight[curr] == min(weight):
        print(sum(length)*weight[curr])
        exit()
    while curr < N-1:
        lens = 0
        for i in range(curr+1,N):
            if weight[curr] >= weight[i]:
                for j in range(curr,i):
                    lens += length[j]
                break
            if i == N-1:
                for k in range(curr,N-1):
                    lens += length[k]
        cost += weight[curr]*lens
        curr = i
    print(cost)
