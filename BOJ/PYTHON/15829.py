import sys
input = sys.stdin.readline

if __name__ == "__main__":
    L = int(input())
    h = 0
    s = input().strip()
    for i in range(L):
        h += (ord(s[i])-96)*(31**i)

    print(h%1234567891)
