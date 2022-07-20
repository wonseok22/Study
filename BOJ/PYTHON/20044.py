import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    i = 0
    j = len(s)-1
    ans = []
    while i<j:
        ans.append(s[i]+s[j])
        i += 1
        j -= 1
    print(min(ans))