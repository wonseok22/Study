

if __name__ == "__main__":
    n = 5#int(input())
    arr1 = [9, 20, 28, 18, 11]#list(map(int,input().split()))
    arr2 = [30, 1, 21, 17, 28]#list(map(int,input().split()))
    answer = ['#'*n for _ in range(n)]
    arr1_cp = [[0]*n for _ in range(n)]
    arr2_cp = [[0]*n for _ in range(n)]
    for i in range(n):
        value = arr1[i]
        for j in range(1,n+1):
            if value%2 == 1:
                arr1_cp[i][-j] = 1
            value = value//2
    for i in range(n):
        value = arr2[i]
        for j in range(1,n+1):
            if value%2 == 1:
                arr2_cp[i][-j] = 1
            value = value//2
    for i in range(n):
        for j in range(n):
            if arr1_cp[i][j] == 0 and arr2_cp[i][j] == 0:
                answer[i][j] = '0'
    for i in range(n):
        print(answer[i])