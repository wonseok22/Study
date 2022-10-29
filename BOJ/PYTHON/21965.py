import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    l = list(map(int,input().split()))
    flag = True
    for i in range(N-1):
        if flag:
            if l[i] >= l[i+1]:
                flag=False
        else:
            if l[i] <= l[i+1]:
                print('NO')
                exit()
    print('YES')
