N, P = map(int,input().split())
a = list(map(int,input().split()))
ans = 0

for i in a:
    if i < P:
        ans += 1

print(ans)
