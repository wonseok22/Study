import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        answer = []
        flag = True
        if N == 1:
            print(N)
            continue
        while N != 1 and flag:
            flag = False
            for i in range(9,1,-1):
                if N % i == 0:
                    answer.append(i)
                    N = N // i
                    flag = True
                    break
        if flag:
            print(len(answer))
        else:
            print(-1)