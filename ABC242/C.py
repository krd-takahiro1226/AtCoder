N = int(input())
dp = [[0] * 9 for _ in range(N)]
dp[0] = [1] * 9
MOD = 998244353
ans_list = []

for i in range(N-1):
    ans = 0
    for j in range(9):
        if j == 0:
            value = (dp[i][j] + dp[i][j+1]) % MOD
        elif j == 8:
            value = (dp[i][j] + dp[i][j-1]) % MOD
        else:
            value = (dp[i][j] + dp[i][j-1] + dp[i][j+1]) % MOD
        dp[i+1][j] = value
        ans += value
    ans_list.append(ans)
print(ans_list[N-2]%MOD)



# 間違った出力
# 3243593152
# 正しい出力
# 248860093
