A, B = map(int,input().split())
if A % B == 0:
    ans = A // B
else:
    ans = A // B + 1
print(ans)
