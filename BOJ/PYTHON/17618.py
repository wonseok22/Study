
print(sum(1 for num in range(1,int(input())+1) if num % sum(map(int,str(num))) == 0))
