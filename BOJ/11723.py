import sys
input = sys.stdin.readline


if __name__ == "__main__":
    result = set()
    for _ in range(int(input())):
        quest = input().strip().split()

        if len(quest) == 1:
            if quest[0] == 'empty':
                result = set()
            else:
                result = set(i for i in range(1, 21))
        else:
            que,val = quest
            val = int(val)
            if que == 'add':
                result.add(val)
            elif que == 'check':
                print(1 if int(quest[1]) in result else 0)
            elif que == 'remove':
                result.discard(val)
            else:
                if val in result:
                    result.discard(val)
                else:
                    result.add(val)


