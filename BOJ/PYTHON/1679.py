
if __name__ == "__main__":
    N = int(input())
    nums = list(map(int,input().split()))
    K = int(input())
    i = 0
    arr = [0]*1020
    for i in nums:
        arr[i] = 1
    print(arr)
    print(nums)
    while True:
        for j in nums:
            if arr[j] + arr[i] < arr[j]+i or arr[j+i] == 0:
                print(arr[j],arr[i])
                arr[j+1] = arr[j]+arr[i]
        if arr[i] > K:
            if i%2 == 0:
                print("holsoon win at"+i)
            else:
                print("jjaksoon win at" + i)
            break
        i+=1