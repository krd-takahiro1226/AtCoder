import math
N, K = map(int,input().split())
A = list(map(int,input().split()))
XY = [list(map(int,input().split())) for _ in range(N)]
light_user = []
remove_cnt = 0
for i in A:
    light_user.append(XY[i-1-remove_cnt])
    del XY[i-1-remove_cnt]
    remove_cnt += 1

user_range = []

for j in range(len(XY)):
    range_list = []
    for k in range(len(light_user)):
        x_diff = XY[j][0] - light_user[k][0]
        y_diff = XY[j][1] - light_user[k][1]
        light_range = math.sqrt(x_diff ** 2 + y_diff ** 2)
        range_list.append(light_range)
    user_range.append(min(range_list))
print(max(user_range))
