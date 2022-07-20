import sys
from itertools import combinations
input = sys.stdin.readline

cards = []
for s1,s2 in list(combinations(input().strip().split(","),2)):
    s = s1+s2
    i1 = int(s1[0],16)
    i2 = int(s2[0],16)
    continued = [-1 if (i1+1)%15 == i2%15 or (i2+1)%15 == i1%15 else 1] # 연속된 경우
    same = [-1 if i1 == i2 else 1] # 같은 경우
    another = [-1 if continued == 1 and same == 1 else 1] # 그 외 경우
    colorSame = [-1 if s1[1] == s2[1] else 1] # 색이 같은 경우
    maxValue = -max(i1,i2) # 큰 수
    minValue = -min(i1,i2) # 작은 수
    maxColor = [s1[1] if i1 > i2 else s2[1]] # 큰 수의 색
    cards.append([continued, same, another, colorSame, maxValue, minValue, maxColor, s])

cards.sort(key = lambda x : (x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
for card in cards:
    print(card[-1])
