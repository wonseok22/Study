import sys
input = sys.stdin.readline

if __name__ == "__main__":
    light = list(input().strip())
    ans = 0
    for i in range(len(light)):
        if light[i] == 'Y':
            for j in range(i,len(light),i+1):
                if light[j] == 'Y':
                    light[j] = 'N'
                else :
                    light[j] = 'Y'
            ans += 1
    print(ans)