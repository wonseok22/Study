import sys
input = sys.stdin.readline

cards = []
conbinations = []
for c in input().split(","):
    cards.append([int("0x"+c[0],16),c[1]])
for i in range(6):
    for j in range(i+1,6):
        conbinations.append(hex(cards[i][0])[2:]+cards[i][1]+hex(cards[j][0])[2:]+cards[j][1])
print(conbinations)