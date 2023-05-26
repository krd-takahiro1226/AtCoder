import itertools
N, M = map(int,input().split())
S = [list(input()) for _ in range(N)]
S.sort()
cnt = 0
ans = False

# 全パターンの並び替えさえできれば、あとは隣り合う要素の差が1かどうかで判定すれば良い
for T in itertools.permutations(S):
    cnt = 0
    for i in range(N-1):
        for j in range(M):
            if T[i][j] != T[i+1][j]:
                cnt += 1
    if cnt == N-1:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")
