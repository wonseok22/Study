import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    line = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if line[i][1] != 0 and line[i][1] != 0:
                if line[i][0]/line[i][1] != line[j][0]/line[j][1]:
                    cnt += 1
            elif line[i][1] == 0 and line[j][1] != 0:
                cnt +=1
            elif line[i][1] != 0 and line[j][1] == 0:
                cnt +=1
    print(cnt)
