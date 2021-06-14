import sys
input = sys.stdin.readline

if __name__ == "__main__":
    L,R = input().split()
    cnt = 0
    if len(L) < len(R):
        print(0)
    else:
        for i in range(len(L)):
            if L[i] != R[i]:
                break
            if L[i] == '8' and R[i] == '8' :
                cnt+=1
        print(cnt)