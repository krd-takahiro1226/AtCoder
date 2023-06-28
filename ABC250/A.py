h, w = map(int,input().split())
r, c = map(int,input().split())
ans = 0
if 1 < r < h:
    ans += 2
elif h == 1:
    ans += 0
else:
    ans += 1

if 1 < c < w:
    ans += 2
elif w == 1:
    ans += 0
else:
    ans += 1
print(ans)
