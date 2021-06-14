import sys
input = sys.stdin.readline

if __name__ == "__main__":
    S = input().strip()
    for i in S:
        cnt=0
        for j in str(ord(i)):
            cnt += int(j)
        print(i*cnt)