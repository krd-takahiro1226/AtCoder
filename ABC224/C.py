from itertools import combinations
N = int(input())
XY = []
ans = 0
for _ in range(N):
    XY.append(list(map(int,input().split())))
XY.sort()
XY_comb = list(combinations(XY,3))
# 組み合わせから一直線に並ぶものを消すやり方(どこかしらにん抜けがあり、ACしない)
# for pro in XY_comb:
#     x_diff = set()
#     y_diff = set()
#     for i in range(2):
#         x_diff.add(pro[i][0] - pro[i+1][0])
#         y_diff.add(pro[i][1] - pro[i+1][1])
#     if len(x_diff) != 1 or len(y_diff) != 1:
#         ans += 1
# print(ans)

# 三角形の面積を求め、それが正になるか判定するやり方
for pro in XY_comb:
    x1 = pro[0][0]
    y1 = pro[0][1]
    x2 = pro[1][0]
    y2 = pro[1][1]
    x3 = pro[2][0]
    y3 = pro[2][1]
    area = abs((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3))
    if area != 0:
        ans += 1
print(ans)
