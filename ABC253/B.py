H, W = map(int,input().split())
ind = []

for i in range(H):
    s = list(input())
    for j in range(len(s)):
        if s[j] == "o":
            ind.append((i+1,j+1))
x_diff = abs(ind[0][0] - ind[1][0])
y_diff = abs(ind[0][1] - ind[1][1])
ans = x_diff + y_diff
print(ans)
