N, M = map(int,input().split())
KA = [list(map(int,input().split())) for _ in range(N)]
A = []
like_list = [0] * (M+1)
ans = 0
for i in range(N):
    A.append(KA[i][1:])

for j in A:
    for k in range(len(j)):
        like_list[j[k]] += 1

for l in like_list:
    if l == N:
        ans += 1
print(ans)
