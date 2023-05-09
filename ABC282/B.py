import itertools
N, M = map(int,input().split())
pep_list = [i for i in range(1,N+1)]
pep_comb = list(itertools.combinations(pep_list,2))
ans = len(pep_comb)
S = []
for _ in range(N):
    S.append(list(input()))

for i in pep_comb:
    for j in range(M):
        if S[i[0]-1][j] == S[i[1]-1][j] == "x":
            ans -= 1
            break
print(ans)
