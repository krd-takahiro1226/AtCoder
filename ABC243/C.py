from collections import defaultdict
N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
S = list(input())
dic = defaultdict(list)
collsion = False

# 同じ高さの人を辞書のkeyで管理、方向と現在のx座標をvalueとして登録
# valueを方向がkey,座標がvalueの辞書にする？→無理そう(keyで場合分けが必要になる)
for i in range(N):
    X = XY[i][0]
    Y = XY[i][1]
    si = S[i]
    dic[Y].append((si,X))
# print(dic)
# 同じ高さの人について、進行方向が逆かつ、ぶつかる可能性がある(お互いの進行方向に人がいる)ものを判定
for keys in dic.keys():
    height_i = dic[keys]
    R_min = 10 ** 9 + 1
# L_minをこれで初期化すると同じ方向に進んでるやつを弾けない
    L_max = 0
    R = []
    L = []
    if len(height_i) >= 2:
        for j in range(len(height_i)):
            dir = height_i[j][0]
            num = height_i[j][1]
            if dir == "R":
                if num < R_min:
                    R_min = num
                R.append(num)
            else:
                if num > L_max:
                    L_max = num 
                L.append(num)
# 計算量的に工夫したい
        if len(R) == 0:
            R_min = 0
        if len(L) == 0:
            L_max = 0
        if L_max > R_min:
            collsion = True
if collsion:
    print("Yes")
else:
    print("No")
