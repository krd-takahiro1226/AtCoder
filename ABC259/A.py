N, M ,X, T, D = map(int,input().split())

if X <= M <N:
    ans = T
else:
    ans = T - (X-M) * D
print(ans)
