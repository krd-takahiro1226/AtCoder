x1,y1,x2,y2 = map(int,input().split())
line_num = max(abs(x1-x2),abs(y1-y2))
x_diff = x2 - x1
y_diff = y2 - y1

x3 = x2 - y_diff
y3 = y2 + x_diff
x4 = x3 - x_diff
y4 = y3 - y_diff

print(x3,y3,x4,y4)
