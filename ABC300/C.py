H, W = map(int,input().split())
C = [list(input()) for _ in range(H)]
N = min(H, W)
ans = [0] * (N+1)

for i in range(H):
    for j in range(W):
        cnt = 0
        if C[i][j] == "#":
            while(i-cnt >= 0 and i+cnt <= H - 1 and j-cnt >= 0 and j+cnt <= W - 1 and C[i-cnt][j-cnt] == "#" and C[i+cnt][j-cnt] == "#" and C[i-cnt][j+cnt] == "#" and C[i+cnt][j+cnt] == "#"):
                cnt += 1
            ans[cnt-1] += 1
ans.pop(0)
print(*ans)
