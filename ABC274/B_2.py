H, W = map(int,input().split())
C = [list(input()) for _ in range(H)]
ans = [0] * W
cnt = 0

for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            ans[j] += 1
print(*ans)
