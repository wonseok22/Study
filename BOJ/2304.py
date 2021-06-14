pli = []
for _ in range(int(input())):
    pli.append(list(map(int,input().split())))
pli.sort(key = lambda x : x[0])
m = pli.index(max(pli,key=lambda x : x[1]))
answer =((pli[-1][0]+1)-pli[0][0])* pli[m][1]
left_pli = pli[:m+1]
right_pli = pli[m:]
i = 1
print(left_pli,right_pli)
while len(left_pli) > 2:
    if left_pli[0][1]<left_pli[i][1]:
        answer -= (left_pli[-1][1]-left_pli[0][1])*(left_pli[i][0]-left_pli[0][0])
        left_pli = left_pli[i:]
        i=1
    else:
        i+=1
i = -2
while len(right_pli) > 2:
    if right_pli[-1][1]<right_pli[i][1]:
        answer -= (right_pli[0][1]-right_pli[-1][1])*(right_pli[-1][0]-(right_pli[i][0]))
        right_pli = right_pli[:i]
        i = -2
    else:
        i-=1
print(answer) 


