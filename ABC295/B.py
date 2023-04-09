R, C = map(int,input().split())
B = [list(input()) for l in range(R)]

for i in range(R):
    for j in range(C):
        if B[i][j].isdigit():
            bomb_num = int(B[i][j])
            for k in range(i - bomb_num, i + bomb_num + 1):
                for l in range(j - bomb_num, j + bomb_num + 1):
                    if 0 < abs(i - k) + abs(j - l) <= bomb_num and 0 <= k < R and 0 <= l < C:
                        # print(k,l)
                        if B[k][l] == "#":
                            B[k][l] = "."
        else:
            continue
for i in range(R):
    for j in range(C):
        if B[i][j] != "#":
            B[i][j] = "."
for b in B:
    print("".join(b))


# 参考にするやつ
# R, C = map(int,input().split())
# B = [list(input()) for _ in range(R)]

# for r in range(R):
#     for c in range(C):
#         if B[r][c] == "." or B[r][c] == "#": continue
#         else:
#             p = int(B[r][c])
#             for i in range(r-p, r+p+1):
#                 for j in range(c-p, c+p+1):
#                     if 0 < abs(i - r) + abs(j - c) <= p and 0 <= i < R and 0 <= j < C:
#                     #print(i, j)
#                         if B[i][j] == "#":
#                             B[i][j] = "."

# for r in range(R):
#     for c in range(C):
#         if B[r][c] != "#":
#             B[r][c] = "."
# for b in B:
#     print("".join(b))

# 間違っているやつ
# 何がダメだったか
# 爆弾の位置を中心にマンハッタン距離を考えるべきだった→二重✖️二重のfor文にするべき
# 二重✖️二重のfor文にすると、後者のfor文を中心から動かせる範囲(座標-爆弾規模から座標＋爆弾規模)で組める
# 二つのfor文の変数と元座標の合計が爆弾規模より小さくなるようにif文を設定(盤面範囲のif文も追加する必要あり)
# for i in range(R):
#     for j in range(C):
#         if B[i][j] != "#" and B[i][j] != ".":
#             bomb_num = int(B[i][j])
#             B[i][j] = "."
#             for k in range(bomb_num+1):
#                 print("bomb_num",bomb_num)
#                 print(bomb_num-k)
#                 print(k)
#                 print(-bomb_num+k)
#                 # if i+k <= R - 1 and j+k <= C - 1 and i-k >= 0 and j-k >= 0 and 0<= j+bomb_num-k <= C-1 and j-bomb_num+k >= 0 and 0<= i+bomb_num-k <= R-1 and i-bomb_num+k >= 0:
#                 if i+k <= R-1 and 0<= j+bomb_num-k <= C-1:
#                     B[i+k][j+bomb_num-k] = "."
#                 if i-k >= 0 and 0<= j+bomb_num-k <= C-1:
#                     B[i-k][j+bomb_num-k] = "."
#                 if i+k <= R-1 and j-bomb_num+k >= 0:
#                     B[i+k][j-bomb_num+k] = "."
#                 if i-k >= 0 and j-bomb_num+k >= 0:
#                     B[i-k][j-bomb_num+k] = "."
#                 if j+k <= C-1 and 0<= i+bomb_num-k <= R-1:
#                     B[i+bomb_num-k][j+k] = "."
#                 if j-k >= 0 and 0<= i+bomb_num-k <= R-1:
#                     B[i+bomb_num-k][j-k] = "."
#                 if j+k <= C-1 and i-bomb_num+k >= 0:
#                     B[i-bomb_num+k][j+k] = "."
#                 if j-k >= 0 and i-bomb_num+k >= 0:
#                     B[i-bomb_num+k][j-k] = "."
#         else:
#             pass
# for i in B:
#     print(*i)
