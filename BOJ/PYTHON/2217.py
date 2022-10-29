num = int(input())
weight = []
for i in range(num):
    a = int(input())
    weight.append(a)
weight.sort(reverse=True)
max_weight = 0
added = 1
for i in range(len(weight)):
    predict = weight[i]*added
    added += 1
    if predict >= max_weight:
        max_weight = predict
print(max_weight)

