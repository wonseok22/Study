import sys
input = sys.stdin.readline

def BinarySearch(lst):
    target = int(input())
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = (start+end)//2
        if lst[mid] < target:
            start = mid + 1
        elif lst[mid] > target:
            end = mid - 1
        else:
            return mid + 1
    return None

if __name__ == "__main__":
    print(BinarySearch(list(map(int,input().split()))))