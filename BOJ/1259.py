import sys
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        N = input().strip()
        if N == '0':
            break
        j = len(N)-1
        flag = False
        for i in range(len(N)//2):
            if N[i] != N[j]:
                flag = True
                print('no')
                break
            j -= 1
        if not flag:
            print('yes')


