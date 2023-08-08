X, Y = map(int,input().split())
diff = Y - X
if diff > 0:
    if diff % 10 == 0:
        ans = diff // 10
    else:
        ans = diff // 10 + 1
else:
    ans = 0
print(ans)
