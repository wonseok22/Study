import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    num = 666
    check = 0
    while True:
        cnt = 0
        for i in str(num):
            if i == '6':
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                check += 1
                break
        if check == N:
            print(num)
            break
        num+=1