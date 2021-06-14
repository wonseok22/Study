import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    for i in range(1,N):
        check = i
        for j in str(i):
            check += int(j)
        if check == N:
            print(i)
            exit()
    print(0)
