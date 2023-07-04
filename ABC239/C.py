x1, y1, x2, y2 = map(int,input().split())
x_diff = [1, 1, -1, -1, 2, 2, -2, -2]
y_diff = [2, -2, 2, -2, 1, -1, 1, -1]
cand_1 = []
cand_2 = []
ans = False

for i in range(8):
    xi_diff = x_diff[i]
    yi_diff = y_diff[i]
    cand_1.append((x1 + xi_diff, y1 + yi_diff))
    cand_2.append((x2 + xi_diff, y2 + yi_diff))

for j in cand_1:
    if j in cand_2:
        ans = True

if ans:
    print('Yes')
else:
    print('No')
