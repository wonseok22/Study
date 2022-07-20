if __name__ == "__main__":
    length,width,height = map(int,input().split())
    num = int(input())
    cube = {}
    x=1

    for _ in range(num):
        x,y = map(int,input().split())
        cube[x] = y
    print(cube)
    x=1
    print(x<<3)
    x <<= 3

    print(x)


