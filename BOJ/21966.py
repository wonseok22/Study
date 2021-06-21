import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    S = input().strip()

    if N <= 25:
        print(S)
    else:
        cnt = 0
        for value in S[11:-11]:
            if value == '.':
                cnt +=1
        if cnt == 0 :
            print(S[:11] + '...' + S[-11:])
        elif cnt == 1:
            if S[-12] =='.':
                print(S[:11] + '...' + S[-11:])
            else:
                print(''.join(S[:11]) + '......' + ''.join(S[-10:]))
        else:
            print(''.join(S[:11]) + '......' + ''.join(S[-10:]))