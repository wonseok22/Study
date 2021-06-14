import sys
input = sys.stdin.readline

def twoD(dice):
    j = 5
    ret = []
    for i in range(3):
        ret.append(min(dice[i], dice[j]))
        j -= 1
    ret.sort()
    ret = ret[:2]
    return ret

def threeD(dice):
    j = 5
    ret = []
    for i in range(3):
        ret.append(min(dice[i],dice[j]))
        j -= 1
    return ret

if __name__ == "__main__":
    n = int(input())
    dice = list(map(int,input().split()))
    td = sum(threeD(dice))
    ta = sum(twoD(dice))

    if n == 1 :
        print(sum(dice) - max(dice))
    elif n == 2:
        print((ta*4) + (td*4))
    else:
        print((td*4) + (ta*4*(2*n-3)) +(min(dice)*(4*(n-1)*(n-2)+(n-2)*(n-2))))
