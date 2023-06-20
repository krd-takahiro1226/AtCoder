N, W = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,W+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j])
        wi = wv[i-1][0]
        vi = wv[i-1][1]
        if j-1+wi <= W:
            dp[i][j-1+wi] = max(dp[i-1][j-1] + vi, dp[i][j-1+wi])

print(dp[N][W])
