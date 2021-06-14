num_of_meeting = int(input())
x = []
for i in range(num_of_meeting):
    start , end = input().split()
    start = int(start)
    end = int (end)
    x.append([start,end])

count = 0
end_time = 0
x.sort(key=lambda x:x[0])
x.sort(key= lambda x:x[1])
for i in range(num_of_meeting):
    if int(x[i][0]) >= end_time:
        end_time = int(x[i][1])
        count +=1
print (count)