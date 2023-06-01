from itertools import combinations
N = int(input())
xy = []
ans = 0
for _ in range(N):
    xy.append(list(map(int,input().split())))

num_list = [i for i in range(N)]
comb_list = list(combinations(num_list,2))

for i,j in comb_list:
    x_diff = xy[i][0] - xy[j][0]
    y_diff = xy[i][1] - xy[j][1]
    if x_diff != 0:
        tilt = y_diff / x_diff
    else:
        tilt = 0
    if -1 <= tilt <= 1:
        ans += 1
print(ans)
