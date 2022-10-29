import sys
input = sys.stdin.readline

def Euclidean(A,B):
    if A % B == 0:
        return B
    else:
        return Euclidean(B,A%B)

if __name__ == "__main__":
    A,B = map(int,input().split())
    GCD = Euclidean(A,B)
    print(GCD)
    print((A*B)//GCD)
