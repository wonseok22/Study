import sys
input = sys.stdin.readline

TC = int(input())
for t in range(TC):
    print("#{}".format(t),sum(value for value in list(map(int,input().split)) if value % 2 == 1))   