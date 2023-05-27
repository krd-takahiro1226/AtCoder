from collections import defaultdict
N, M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(M)]
dic = defaultdict(set)
ans = 0

for i in range(M):
    for j in range(N):
        if j+1 < N:
            dic[a[i][j]].add(a[i][j+1])
        if 0<= j-1:
            dic[a[i][j]].add(a[i][j-1])

for value in dic.values():
    if len(value) != N - 1:
        ans += N - len(value) - 1
print(ans//2)
