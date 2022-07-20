import sys
input = sys.stdin.readline

if __name__ == "__main__":
    x,y,w,h = map(int,input().split())
    print(min(w-x,x,y,h-y))