import sys
import math
input = sys.stdin.readline

if __name__ == "__main__":
    A,B,V = map(int,input().split())
    print(math.ceil((V-B)/(A-B)))
