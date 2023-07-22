N, M = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(N)]
ans = True
pos_x = [[0] * M for _ in range(N)]
pos_y = [[0] * M for _ in range(N)]

# 表の端を跨ぐようなケースが存在するから、前後の差を取るのでは不十分
# Ai,jの場所は一意に定まる→各要素について座標特定→四角形か判定
for i in range(N):
    for j in range(M):
        val = B[i][j]
        x = (val - 1) % 7 + 1
        # x = (val + 6) % 7 + 1
        y = (val - 1) // 7 + 1
        pos_x[i][j] = x
        pos_y[i][j] = y

for i in range(N):
    for j in range(M):
        if i > 0 and (pos_x[i][j] != pos_x[i-1][j] or pos_y[i][j] != pos_y[i-1][j] + 1):
            ans = False
        if j > 0 and (pos_x[i][j] != pos_x[i][j-1] + 1 or pos_y[i][j] != pos_y[i][j-1]):
            ans = False

if ans:
    print('Yes')
else:
    print('No')
