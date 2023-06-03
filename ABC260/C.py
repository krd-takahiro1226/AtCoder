N,X,Y = map(int,input().split())
# 長さがレベルに対応、入っている数字は個数
red = [0] * (N+1)
blue = [0] * (N+1)

# 公式解説(redがi個あるときに青のレベル1が何個取得できるかを配列に記憶していく)
# red[1] = 0
# blue[1] = 1
# for i in range(2,N+1):
#     blue[i] += red[i-1] + Y * blue[i-1]
#     red[i] += red[i-1] + X * blue[i]

# print(red[N])

red[N] = 1
for i in range(N,1,-1):
    red[i-1] += red[i]
    blue[i] += red[i] * X
    red[i-1] += blue[i]
    blue[i-1] += blue[i] * Y
# ↓がなぜダメか→赤の変換を行ってから出ないと青の個数が確定しないから
    # red[i-1] += red[i] + blue[i]
    # blue[i-1] += Y * blue[i] + X * red[i-1]

print(blue[1])
