N, M = map(int,input().split())
S = []
T = []
ans = 0

for _ in range(N):
    Si = input()
    S.append(Si[-3:])
for _ in range(M):
    Ti = input()
    T.append(Ti)
for s in S:
    if s in T:
        ans += 1
print(ans)
