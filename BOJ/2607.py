if __name__ =="__main__":
    N = int(input())
    words = [input() for _ in range(N)]
    sorted_words = []
    for i in range(N):
        sorted_words.append(sorted(words[i]))
    for i in range(2,N,1):
        if sorted_words[0] == sorted_words[i]:
            answer += 1
        else: