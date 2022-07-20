import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N,M = map(int,input().split())
    true = list(map(int,input().split()))
    people = [list(map(int,input().split())) for _ in range(M)]
    ans = 0
    nPeople = []
    if len(true) == 1:
        print(M)
    else:
        true = true[1:]
        for idx,value in enumerate(people):
            people[idx] = people[idx][1:]
        for _ in range(M):
            for idx in people:
                if len(idx) != len(list(set(idx) - set(true))):
                    true += idx
        true = set(true)
        for i in people:
            if len(i) == len(list(set(i)-true)):
                ans +=1
        print(ans)



