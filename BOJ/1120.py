A,B = input().split()
A=list(A)
B=list(B)
min_diff = 0
diff = 0
for i in range(len(A)):
    if A[i]!=B[i]:
        min_diff+=1
for i in range(1 , len(B)-len(A)+1):
    for j in range(len(A)):
        if A[j] != B[j+i]:
            diff +=1
    if min_diff > diff:
        min_diff = diff
        diff=0;
    else:
        diff=0
print(min_diff)