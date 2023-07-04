N, X = map(int,input().split())
dp = [[False] * (X + 1) for _ in range(N+1)]
iteration = X + 1
dp[0][0] = True

for i in range(N):
    a, b = map(int,input().split())
    for j in range(iteration):
        if j+a < iteration and j+b < iteration and dp[i][j]:
            dp[i+1][j+a] = True
            dp[i+1][j+b] = True
        elif j+a < iteration and dp[i][j]:
            dp[i+1][j+a] = True
        elif j+b < iteration and dp[i][j]:
            dp[i+1][j+b] = True

if dp[N][X]:
    print('Yes')
else:
    print('No')
