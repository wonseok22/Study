import sys
input = sys.stdin.readline

def QuickSort(lst):
    if len(lst) <= 1:
        return lst
    pivotPoint = lst[len(lst)//2]
    left,right,mid = [],[],[]
    for num in lst:
        if num > pivotPoint:
            right.append(num)
        elif num < pivotPoint:
            left.append(num)
        else:
            mid.append(num)
    return QuickSort(left) + mid + QuickSort(right)


if __name__ == "__main__":
    print(QuickSort(list(map(int,input().split()))))