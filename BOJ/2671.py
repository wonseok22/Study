import re
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    p = re.compile('(100+1+|01)+')
    a = input().strip()
    m = p.fullmatch(a)
    if m == None:
        print('NOISE')
    else:
        print('SUBMARINE')