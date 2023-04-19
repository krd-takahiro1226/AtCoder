N, W = map(int,input().split())
wv = [list(map(int, input().split())) for l in range(N)]
dp = [[0] * (W*2) for _ in range(N+1)]
dp[0][0] = 1

# 最後に1引く
for i in range(1,N+1):
    for j in range(1,W+1):
        if dp[i-1][j-1] != 0:
            dp[i][j+wv[i-1][0]-1] = max(dp[i][j+wv[i-1][0]-1], dp[i-1][j-1] + wv[i-1][1])
            if dp[i][j-1] < dp[i-1][j-1]:
                dp[i][j-1] = dp[i-1][j-1]
ans_cand = dp[N]
ans = ans_cand[0]

for i in range(1,W+1):
    if ans_cand[i] > ans:
        ans = ans_cand[i]
    else:
        pass
print(ans-1)
