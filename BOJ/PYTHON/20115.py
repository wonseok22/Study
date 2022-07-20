import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    drink = sorted(list(map(int,input().split())))
    if sum(drink[:-1])%2 == 0:
        print(drink[-1] + int(sum(drink[:-1])/2))
    else:
        print(drink[-1] + sum(drink[:-1])/2)

