import sys
input = sys.stdin.readline

def findpath(N):
    num = 1
    cnt = 0
    if N >= 1023:
        return -1
    if N == 0:
        return cnt
    while True:
        length = str(num)
        f = True
        print(num)
        if len(length) == 1:
            pass
        else:

            for i in range(1,len(length)):
                if int(length[i]) < int(length[i-1]): # 감소하는 수 인지
                    continue
                else:
                    start = length[:i - 1]
                    mid = str(int(length[i - 1]) + 1)
                    end = '0' + length[i + 1:]
                    num = int(start + mid + end)
                    f = False
                    break
        if f:
            cnt +=1
            if cnt == N:
                return num
            num += 1

if __name__ == "__main__":
    N = int(input())
    print(findpath(N))
