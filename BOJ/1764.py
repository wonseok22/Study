if __name__ == "__main__":
    N,M = map(int,input().split())
    D = []
    B = []
    for _ in range(N):
        D.append(input())
    for _ in range(M):
        B.append(input())
    answer = list(set(D) & set(B))
    print(len(answer))
    answer.sort()
    for n in answer:
        print(n)