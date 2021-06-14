# 무게 M 가격 V 가방 K개 가방의 수용량 C 보석의 개수 최대 1개
# 첫째 줄 N , K 주어짐
# 다음 N 줄은 M과 V가 주어짐
# 다음 K개의 줄 각각 C가 주어짐

def jewelry():
    for i in range(N):
        M, V = input().split()
        N_list.append((int(M),int(V)))

def weight():
    for i in range(K):
        C = int(input())
        C_list.append(C)

def findmax():
    sums = 0
    for i in range(min(N,K)):
        for j in range(len(C_list)):
            if N_list[i][0]<= C_list[j]:
                sums += N_list[i][1]
                del C_list[j]
                break
    print(sums)
N, K = input().split()
N_list = []
C_list = []
N= int(N)
K= int(K)
jewelry()
weight()
C_list.sort()
N_list.sort(key = lambda x: x[1],reverse = True)
findmax()