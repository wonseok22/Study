import re
t1 = input()
t2 = input()
text = re.findall(t2,re.sub("[0-9]","",t1))
if text:
    print(1)
else:
    print(0)
