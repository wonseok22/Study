import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    ans = 0
    if sorted(A) != sorted(B):
        print(-1)
        exit()
    curr = len(A)-1
    if curr == 0 :
        if A == B:
            print(0)
        else:
            print(-1)
        exit()
    for i in range(len(A)-1,-1,-1):
        if A[i] != B[curr]:
            ans += 1
        else:
            curr -= 1
    print('<'+', '.join(map(str,ans))+'>')
    print('. ')