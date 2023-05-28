xy = [list(map(int,input().split())) for _ in range(3)]
x = []
y = []

for i in range(3):
    x.append(xy[i][0])
    y.append(xy[i][1])

x_unique = set(x)
y_unique = set(y)

for j in x_unique:
    if x.count(j) == 1:
        ans_x = j

for k in y_unique:
    if y.count(k) == 1:
        ans_y = k

print(ans_x,ans_y)
