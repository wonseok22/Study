import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,M = map(int,input().split())
    ans = []
    for i in range(N,M+1):

        flag = True
        if i == 1:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            ans.append(i)

    for i in ans:
        print(i)