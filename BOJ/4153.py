import sys
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        length = sorted(list(map(int,input().split())))
        if length[0] == 0:
            break
        if length[0]**2 + length[1]**2 == length[2]**2:
            print('right')
        else:
            print('wrong')