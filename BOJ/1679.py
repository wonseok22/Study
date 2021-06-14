from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int,input().split()))
    K = int(input())
    nums = nums*K
    S = []
    for i in range(1,K+1):
        L = list(combinations(nums,i))
        for idx in L:
            S.append(sum(idx))
    S = list(set(S))
    for idx in range(len(S)):
        if S[idx] != idx+1:
            if idx%2 == 1:
                print("holsoon win at",idx+1)
            else:
                print("jjaksoon win at",idx+1)
            break