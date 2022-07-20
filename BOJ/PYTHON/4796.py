if __name__ == "__main__":
    case = 1
    while True:
        L,P,V = map(int,input().split())
        if L == 0 and P == 0 and V == 0:
            break
        answer = (V//P)*L+min(L,V%P)
        print("Case",case,end='')
        print(":",answer)
        case += 1