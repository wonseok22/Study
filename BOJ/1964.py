N = int(input())
print(sum([(3*n)+1 for n in range(N+1)])%45678)