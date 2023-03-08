import itertools

N, M = map(int,input().split()) 
A = [list(map(int, input().split())) for l in range(M)]
k = [0] * M
X = []
all_comb = []
X_comb = []
count = 0
win_ind = []

for i in range(M):
    k[i] = A[i][0]

for j in range(len(k)):
    x_k = list(A[j][1 : k[j] + 1])
    X.append(x_k)

k_i_cand = list(range(N + 1))
k_i_cand.remove(0)
k_i_cand_comb = itertools.combinations(k_i_cand, 2)
for comb in k_i_cand_comb:
    all_comb.append(comb)
# 全組み合わせあるか考えないといけない
for i in range(M):
    X_i_comb = itertools.combinations(X[i], 2)
    for comb in X_i_comb:
        X_comb.append(comb)
for j in all_comb:
    if j in X_comb:# X[i]だと組み合わせが取れていない。全要素[1,2,3]みたいな感じになってしまい、2つの組になっていない
        win_ind.append(all_comb.index(j))
    else:
        pass
for num in range(len(all_comb)):
    if (num in win_ind):
        count = count + 1
    else:
        pass

if count == len(all_comb):
    print("Yes")
else:
    print("No")
