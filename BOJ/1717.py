import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n,m = map(int,input().split())
    L = [list(map(int,input().split())) for _ in range(m)]
    sets = [[i] for i in range(n+1)]
    for idx,a,b in L:
        print(sets)
        if idx == 0:
            sets[a] = list(set(sets[a] + sets[b]))
            sets[b] = list(set(sets[a] + sets[b]))
        else:
            flag = False
            for key in sets[a]:
                if key == b:
                    flag = True
            for key in sets[b]:
                if key == a:
                    flag = True
            if flag:
                print('YES')
            else:
                print('NO')
