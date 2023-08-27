N = int(input())
XYZ = [list(map(int,input().split())) for _ in range(N)]
all_giseki = 0
takahashi = 0
aoki = 0
INF = 10 ** 20
W = [0] * (N+1)

for i in range(N):
    all_giseki += XYZ[i][2]
    xyz = XYZ[i]
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    val = (y + x) // 2 + 1 - x
    if x > y:
        takahashi += z
        W[i] = 0
    else:
        aoki += z
        W[i] = val
need_giseki = all_giseki // 2 + 1

dp = [INF] * (all_giseki+1)
dp[0] = 0

if takahashi > aoki:
    print(0)
else:
    for i in range(1, N+1):
        xyz = XYZ[i-1]
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        val = (y + x) // 2 + 1 - x
        for j in range(all_giseki, z-1, -1):
            dp[j] = min(dp[j], dp[j-z]+W[i-1])
    print(min(dp[need_giseki:]))
