N,D = map(int,input().split())
answer = 0
for i in range(1,N+1): # 1부터 N까지의 숫자를 탐색
    s_i = str(i) # 자릿수 연산을 위해 문자열로 변환
    l = len(s_i)
    for sliceCnt in range(l):  #몇 자릿수로 자르는지 range : 1 ~ len(i)
        for x in range(l-sliceCnt):  # 자르는 시작점
            s = s_i[x]
            for y in range(sliceCnt): # 자르는 자릿수
                s += s_i[x+y]
            if s == str(D):
                answer += 1
print(answer)