A, B, C = map(int,input().split())
max = max(A, B, C)
min = min(A, B, C)
mid = A + B + C - max - min
max_min = max - min
max_mid = max - mid

if (max_min - max_mid) % 2 == 0:
    ans = (mid-min) // 2 + max_mid
else:
    # ans = 1 + (mid-min) // 2 + max_mid
    ans = 1 + max_mid + ((max_min+1) - max_mid) // 2
print(ans)
