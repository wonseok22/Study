import sys
input = sys.stdin.readline
N, M = map(int,input().split())
price = sorted([list(map(int,input().split())) for _ in range(N)], key = lambda x : (x[1],-x[0]))
if price[0][0] >= M: # 가격이 제일 싼 고기 하나만 사도 만족하는 경우
    print(price[0][1])
    exit()
s = price[0][0]
tmp = [0] # 같은 가격의 고기들의 인덱스를 저장하기 위함
for i in range(1,N):
    s += price[i][0]
    if price[tmp[-1]][1] == price[i][1]:
        tmp.append(i)
    else:
        tmp = [i]
    if s >= M:
        if price[i-1][1] < price[i][1]: # 현재 사려는 고기까지 사면 M을 충족하며, 그 전 고기의 가격이 현재 사려는 고기보다 싼 경우
            print(price[i][1])
            exit()
        else: # 현재 사려는 고기와 같은 가격의 고기가 여러개일 경우
            total_price = price[tmp[0]][1] * len(tmp)
            while i < N and price[tmp[0]][1] ==  price[i][1]: # 그 다음으로 비싼 고기를 사는 가격
                i += 1
            if i < N: # 그 다음으로 비싼 고기가 있다면
                print(min(price[i][1], total_price)) # 같은가격의 고기를 모두 사는것 vs 그 다음으로 비싼 고기를 사는 것 비교
            else:
                print(total_price) # 다음으로 비싼 고기가 없으면 어쩔 수 없이 같은가격의 고기를 사야됨
                
                
            exit()

print(-1)
