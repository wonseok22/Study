import sys
flush = sys.stdout.flush
p = print
N,t = map(int,input().split())
x = [(N+1)//2,N//2+1]
y = [(N+1)//2,(N+1)//2-1]
p("!", x[t])
flush()
if t==1:
    p(1, 1)
    flush()
for _ in range(y[t]):
    a,b = map(int,input().split())
    p(b,a)
    flush()
