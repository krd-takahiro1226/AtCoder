N, K = map(int,input().split())
h = list(map(int,input().split()))
INF = 10**19
dp = [INF] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

# chmin
for i in range(2,N):
    for k in range(1,K+1):
        if 0 <= i-k < N:
            dp[i] = min(dp[i-k] + abs(h[i] - h[i-k]), dp[i])
# print(dp)
print(dp[N-1])
