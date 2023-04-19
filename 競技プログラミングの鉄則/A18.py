N, S = map(int,input().split())
A = list(map(int,input().split()))
dp = [[0] * (10**5) for _ in range(N+1)]
dp[0][0] = 1
cnt = 0
ans = False

# 2次元のdp
# 縦を上から何枚目までのカードを使うか(長さ:N+1,1オリジン)
# 横を取りうる合計の値なら1、取らないなら0のリスト(長さ:10**5,条件的に2*10**4あれば十分だと思われる)

for i in range(1,N+1):
    for j in range(1,S+1):
        if dp[i-1][j-1] == 1:
            dp[i][j-1] = 1
            dp[i][j+A[i-1]-1] = 1

for i in range(N+1):
    if dp[i][S] == 1:
        ans = True
    else:
        pass
if ans:
    print("Yes")
else:
    print("No")
