N, X = map(int,input().split())
P = list(map(int,input().split()))
ans = []
for i in range(N):
    if P[i] == X:
        ans.append(i+1)

print(*ans)
