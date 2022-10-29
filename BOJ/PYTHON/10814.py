import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    age = sorted([list(input().split()) for _ in range(N)],key = lambda x : int(x[0]))
    for a,name in age:
        print(int(a),name)