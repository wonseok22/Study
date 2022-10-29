import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n,m = map(int,input().split())
    card = list(map(int,input().split()))
    for i in range(m):
        card.sort()
        s = card[0] + card[1]
        card[0] = s
        card[1] = s
    print(sum(card))

