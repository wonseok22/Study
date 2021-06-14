import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    check = 1
    i = 1
    if N == 1:
        print(1)
        exit()
    while check < N:
        check += 6*i
        i += 1
    print(i)