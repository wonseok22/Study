from itertools import combinations
import sys
input = sys.stdin.readline


def cnt(c,n):

    cou = 0
    for i in n:
        flag = True
        for j in i:
            if j not in c:
                flag=False
        if flag :
            cou += 1
    return cou

if __name__ == "__main__":
    N,K = map(int,input().split())
    l = [input().strip()[4:-4] for _ in range(N)]
    alpha = {}
    for i in range(97,96+27,1):
        alpha[chr(i)] = 0
    alpha['a'] = 1
    alpha['n'] = 1
    alpha['t'] = 1
    alpha['i'] = 1
    alpha['c'] = 1
    K -= 5
    n = []
    for i in l:
        st = ''
        for key in i:
            if alpha[key] == 0:
                st += key
        n.append(st)
    if K<=0:
        print(n.count(''))
    else:
        st = []
        for i in n:
            for k in i:
                st.append(k)
        c = list(combinations(set(st),K))
        m = 0
        for check in c:
            m = max(m,cnt(check,n))
        print(m)


