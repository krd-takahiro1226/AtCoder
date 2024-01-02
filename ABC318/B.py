N = int(input())
ABCD = [list(map(int,input().split())) for _ in range(N)]
square = [[0] * 100 for _ in range(100)]
ans = 0

for i in range(N):
    a = ABCD[i][0]
    b = ABCD[i][1]
    c = ABCD[i][2]
    d = ABCD[i][3]
    x_diff = b - a
    y_diff = d - c
    Si = x_diff * y_diff
    for j in range(a,b):
        for k in range(c,d):
            square [j][k] = 1
for l in square:
    ans += sum(l)
print(ans)
