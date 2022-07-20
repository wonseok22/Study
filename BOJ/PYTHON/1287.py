S = input()
if S.find("()") != -1:
    print("ROCK")
    exit()
rep = '&'
check = S.replace('/', rep).replace('-', rep).replace('+', rep).replace('*', rep)

try:
	eval(check)
except:
	print("ROCK")
	exit()

try :
    print(eval(S.replace("/","//")))
except:
    print("ROCK")