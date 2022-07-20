N, C = map(int,input().split())
arr = list(map(int,input().strip().split()))
print(' '.join(map(str,sorted(arr,key = lambda x : (arr.count(x),-arr.index(x)), reverse=True))))
