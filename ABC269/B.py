S = [list(input()) for _ in range(10)]
cnt = 0
ans_AB = []
ans_CD = []

for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            ans_AB.append(i+1)
            ans_CD.append(j+1)
ans_AB = [min(ans_AB),max(ans_AB)]
ans_CD = [min(ans_CD),max(ans_CD)]
print(*ans_AB)
print(*ans_CD)
