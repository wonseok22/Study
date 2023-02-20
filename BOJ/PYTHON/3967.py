import sys
input = sys.stdin.readline


def solve(count, curr):
    global answer
    if answer:
        return

    if count == 12:
        answer = True
        for line in star:
            print("".join(line))

    for k in range(curr,12):
        i,j,edges = vertex[k]
        if star[i][j] == "x":
            for value in range(1, 13):
                if not visited[value] and lines[edges[0]][1] + value < 27 and lines[edges[1]][1] + value < 27:
                    if (lines[edges[0]][0] + 1 == 4 and lines[edges[0]][1] + value < 26) or (lines[edges[1]][0] + 1 == 4 and lines[edges[1]][1] + value < 26):
                        continue
                    visited[value] = True
                    star[i][j] = chr(ord("A") + value - 1)
                    lines[edges[0]][0] += 1
                    lines[edges[1]][0] += 1
                    lines[edges[0]][1] += value
                    lines[edges[1]][1] += value
                    solve(count+1, curr+1)
                    visited[value] = False
                    lines[edges[0]][0] -= 1
                    lines[edges[1]][0] -= 1
                    lines[edges[0]][1] -= value
                    lines[edges[1]][1] -= value
                    star[i][j] = "x"
            else:
                return


star = [list(input().strip()) for _ in range(5)]
value = [[0 for _ in range(9)] for _ in range(5)]
visited = [False for _ in range(13)]
answer = False
count = 0
lines = [[0,0] for _ in range(6)] # 삼각형 -> 역삼각형
vertex = [
    [0,4,[0,2]],
    [1,1,[3,5]],
    [1,3,[0,5]],
    [1,5,[2,5]],
    [1,7,[4,5]],
    [2,2,[0,3]],
    [2,6,[2,4]],
    [3,1,[0,1]],
    [3,3,[1,3]],
    [3,5,[1,4]],
    [3,7,[1,2]],
    [4,4,[3,4]],
]


for i,j,edges in vertex:
    if star[i][j] != 'x':
        count += 1
        alpha_to_num = ord(star[i][j]) - ord('A') + 1
        value[i][j] = alpha_to_num
        visited[alpha_to_num] = True
        for e in edges:
            lines[e][1] += alpha_to_num
            lines[e][0] += 1
solve(count, 0)
