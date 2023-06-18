X, Y, Z = map(int,input().split())
S = list(input())
INF = 10 ** 18
dp = [[INF] * 2 for _ in range(len(S)+1)]
dp[0][0] = 0
dp[0][1] = Z
# caps lockを押す動作は含めなくて良い(最後に+Zするのは帳尻合わせでしかなく、次のiの時に考えればよい)
for i in range(1,len(S)+1):
    if S[i-1] == "a":
        dp[i][0] = min(dp[i-1][0] + X, dp[i-1][1] + Z + X, dp[i-1][1] + Y + Z, dp[i][0])
        dp[i][1] = min(dp[i-1][1] + Y, dp[i-1][0] + X + Z, dp[i-1][0] + Z + Y, dp[i][1])
    else:
        dp[i][0] = min(dp[i-1][0] + Y, dp[i-1][1] + X + Z, dp[i-1][1] + Z + Y, dp[i][0])
        dp[i][1] = min(dp[i-1][1] + X, dp[i-1][0] + Z + X, dp[i-1][0] + Y + Z, dp[i][1])

print(min(dp[len(S)]))





# caps = False
# ans_1 = 0
# ans_2 = 0
# # a_w_caps:caps機能を使用して入力
# # a_wo_caps:caps機能を使用しないで入力

# for i in S:
#     if i == "A":
#         if caps:
#             a_w_caps = X
#             a_wo_caps = Z + Y
#         else:
#             a_w_caps = Z + X
#             a_wo_caps = Y
#     else:
#         if caps:
#             a_w_caps = Y
#             a_wo_caps = Z + X
#         else:
#             a_w_caps = Z + Y
#             a_wo_caps = X
#     if a_w_caps < a_wo_caps and caps == False:
#         caps = True
#         ans_1 += a_w_caps
#     elif a_w_caps < a_wo_caps and caps == True:
#         caps = False
#         ans_1 += a_w_caps
#     else:
#         ans_1 += a_wo_caps

# caps = True
# ans_2 += Z
# for i in S:
#     if i == "A":
#         if caps:
#             a_w_caps = X
#             a_wo_caps = Z + Y
#         else:
#             a_w_caps = Z + X
#             a_wo_caps = Y
#     else:
#         if caps:
#             a_w_caps = Y
#             a_wo_caps = Z + X
#         else:
#             a_w_caps = Z + Y
#             a_wo_caps = X
#     if a_w_caps < a_wo_caps and caps == False:
#         caps = True
#         ans_2 += a_w_caps
#     elif a_w_caps < a_wo_caps and caps == True:
#         caps = False
#         ans_2 += a_w_caps
#     else:
#         ans_2 += a_wo_caps

# print(min(ans_1,ans_2))
