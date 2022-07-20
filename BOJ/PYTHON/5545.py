import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a,b = map(int,input().split())
    c = int(input())
    topping = [int(input()) for _ in range(n)]
    topping.sort(reverse = True)
    cal = c
    price = a
    for val in topping:
        if cal/price < val/b:
            cal = cal+val
            price += b
        else:
            break
    print(cal//price)