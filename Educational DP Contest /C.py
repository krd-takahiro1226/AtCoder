N = int(input())
dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    a,b,c = map(int,input().split())
    if i == 0:
        dp[i][0] = a
        dp[i][1] = b
        dp[i][2] = c
    else:
        dp[i][0] = max(dp[i-1][1] + a, dp[i-1][2] + a)
        dp[i][1] = max(dp[i-1][0] + b, dp[i-1][2] + b)
        dp[i][2] = max(dp[i-1][0] + c, dp[i-1][1] + c)

print(max(dp[N-1]))
