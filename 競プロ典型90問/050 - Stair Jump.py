N, L = map(int,input().split())
dp = [0] * (2*10**5)
# dp = [0] * (2*10**1)
dp[1] = 1
dp[L] = 1

for i in range(1,N+1):
    if dp[i] != 0:
        dp[i+1] += dp[i]
        dp[i+L] += dp[i]
# print(dp)
print(dp[N] % ((10 ** 9) + 7))
