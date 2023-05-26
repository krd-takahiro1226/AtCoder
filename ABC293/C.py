from itertools import product
H, W = map(int,input().split())
A = [list((map(int,input().split()))) for _ in range(H)]
iter_num = H + W - 2 
ans = 0

for pro in product((0,1),repeat=iter_num):
    visit = set()
    x = 0
    y = 0
    visit.add(A[x][y])
    for i in pro:
        if 0 <= x < W and 0 <= y < H:
            if i == 0:
                x += 1
            else:
                y += 1
        if 0 <= x < W and 0 <= y < H:
            visit.add(A[y][x])
    if len(visit) == iter_num + 1:
        ans += 1
print(ans)
