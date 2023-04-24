N = int(input())
S = list(input())
color = [False] * N
cnt = 1
ans = []
# 0:白、1:青、2:赤
# 最後の塗る作業で連続する3つのタイルが存在するはず
# 連続する3つのタイルが存在 → 目的達成できる、連続する3つのタイルが存在しない → 目的達成できない
for i in range(N-1):
    color_i = S[i]
    if color_i == S[i+1]:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 1
ans.append(cnt)

if max(ans) >= 3:
    print("Yes")
else:
    print("No")



# 自分で実装(後ろ(前でも良い？)から見ていって、連続する3つを塗る → その結果できる配列が理想と一致したらYesを出力)
# ↑ 間違っている(片方から攻めるだけでは十分じゃない、入力例1の時などに詰まる)
# for j in range(N):
#     i = N - j - 1
#     if S[i] == "R":
#         color[i] = "R"
#         color[i-1] = "R"
#         color[i-2] = "R"
#     elif S[i] == "B":
#         color[i] = "B"
#         color[i-1] = "B"
#         color[i-2] = "B"
# if color == S:
#     print("Yes")
# else:
#     print("No")
# print(color)
# print(S)
