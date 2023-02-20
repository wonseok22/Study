import sys
input = sys.stdin.readline

N = int(input())
for word in sorted(list(input().strip() for _ in range(N)), key = lambda x : (len(x), sum(int(i) for i in x if i.isdigit()), x)):
    print(word)

