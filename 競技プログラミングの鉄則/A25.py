H, W = map(int,input().split())
C = [list(input()) for _ in range(H)]
dp = [[0] * W for _ in range(H)]

# 1番外側の処理がミスってたっぽい？→新しい配列(ここでいうdp)を使わず、Cの中で処理していたから？
# 本質的な処理部分は間違っていなかった
for k in range(H):
    if C[k][0] == "#":
        break
    dp[k][0] = 1

for l in range(W):
    if C[0][l] == "#":
        break
    dp[0][l] = 1

for i in range(1,H):
    for j in range(1,W):
        if C[i][j] == ".":
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        elif C[i][j] == "#":
            dp[i][j] = 0
print(dp[H-1][W-1])

# Chat GPT出力コード(ACする)
# H, W = map(int,input().split())
# C = [list(input().strip()) for _ in range(H)]
# dp = [[0]*W for _ in range(H)]

# # 左端と上端の初期化
# for i in range(H):
#     if C[i][0] == "#":
#         break
#     dp[i][0] = 1

# for j in range(W):
#     if C[0][j] == "#":
#         break
#     dp[0][j] = 1

# # 動的計画法
# for i in range(1, H):
#     for j in range(1, W):
#         if C[i][j] == "#":
#             dp[i][j] = 0
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]

# print(dp[-1][-1])
