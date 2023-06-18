N = int(input())
INF = 10**18
dp = [[-INF] * 2 for _ in range(N+1)]
dp[0][0] = 0

# 遷移先候補と今の値を比べて大きい方を採用する
for i in range(1,N+1):
    x,y = map(int,input().split())
# 現状でいいか、食べない方がよかったかを判定
    dp[i][0] = max(dp[i][0],dp[i-1][0])
# 毒状態の時は、毒が食べれないので前の値を引き継ぐ
    dp[i][1] = dp[i-1][1]
# 毒状態から解毒を食べるor健康で解毒食べるor現状の美味しさの総和の中から最大を選択
    if x == 0:
        dp[i][0] = max(dp[i-1][1] + y, dp[i-1][0] + y, dp[i][0])
# 健康から毒入りを食べるor現状の美味しさの総和の中から最大を選択
    else:
        dp[i][1] = max(dp[i-1][0] + y, dp[i][1])

print(max(dp[N][1],dp[N][0]))
