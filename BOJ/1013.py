import re,sys
input = sys.stdin.readline

for _ in range(int(input())):
    S = input().strip()
    compile = re.compile('(100+1+|01)+')
    match = compile.fullmatch(S)
    if match: print("YES")
    else: print("NO")

