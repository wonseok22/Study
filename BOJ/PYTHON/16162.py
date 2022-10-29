import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,A,D = map(int,input().split())
    n = list(map(int,input().split()))
    ans = []
    cnt = 0
    curr = A
    for i in n:
        if i == curr:
            cnt +=1
            curr += D
        ans.append(cnt)
    print(max(ans))