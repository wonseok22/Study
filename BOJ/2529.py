cnt = int(input())
k = []
x = input()
k = x.split()
obj = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
num = 9

def findmax(i):
    global num
    global before
    if k[i] == '<' and k[i+1] == '<':
        findmax(i+1)
        obj[i+1]=num
        num-=1
        print(i+1,num+1)
    else:
        obj[i+1] = num
        num-=1
        print(i+1,num+1)
findmax(0)
before=0
for i in range(cnt):
    if k[i]=='<' and before == 0:
        findmax(i)
        before = 1
    elif k[i] == '>':
        before = 0


print(k)
print(obj)
print(obj[2])
