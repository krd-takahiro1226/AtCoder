# H, W = map(int,input().split()) 
# c = [list(map(int, input().split())) for l in range(W)]

H = 3
W = 4

c = [["#", ".", ".", "#"], [".", "#", ".", "#"], [".", "#", ".", "#"]]

# score_ind = ([i for i, x in enumerate(c[0]) if x == '#'])

X_score = []
for j in range(W):
    score = 0
    for i in range(H):
        if c[i][j] == ".":
            score = score + 0
        elif c[i][j] == "#":
            score = score + 1
    X_score.append(score)

# for k in X_score:
#     print(k, end='')
print(*X_score)
