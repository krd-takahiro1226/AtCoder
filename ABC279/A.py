S = list(input())
ans = 0
for i in S:
    if i == "v":
        ans += 1
    else:
        ans += 2
print(ans)
