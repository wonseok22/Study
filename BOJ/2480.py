A,B,C = map(int,input().split())
if A==B and B==C:
    print(A*1000+10000)
elif A==B:
    print(A*100 + 1000)
elif B==C:
    print(B*100 + 1000)
elif A==C:
    print(A*100 + 1000)
else:
    print(max(A,B,C)*100)