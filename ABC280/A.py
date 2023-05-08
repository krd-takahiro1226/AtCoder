H, W = map(int,input().split())
ans = 0
for _ in range(H):
    S = list(input())
    for i in S:
        if i == "#":
            ans += 1
print(ans)
