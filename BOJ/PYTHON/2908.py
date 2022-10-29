A,B = input().split()
for i in range(-1,-4,-1):
    if A[i] > B[i]:
        print(A[-1]+A[-2]+A[-3])
        break
    elif A[i] < B[i]:
        print(B[-1] + B[-2] + B[-3])
        break


