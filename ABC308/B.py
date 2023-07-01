N, M = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))
D_unique = set(D)
ans = 0

for i in range(N):
    if C[i] in D_unique:
        ind = D.index(C[i])
        ans += P[ind+1]
    else:
        ans += P[0]
print(ans)
