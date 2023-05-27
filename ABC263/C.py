from itertools import combinations
N , M = map(int,input().split())
num_list = (i for i in range(1,M+1))
ans = []

# itertoolの組み合わせ列挙は、渡したリストに則る辞書順で列挙される
for pro in combinations(num_list,N):
    cnt = 0
    for j in range(N-1):
        if pro[j] < pro[j+1]:
            cnt += 1
    if cnt == N - 1:
        ans.append(pro)

for k in ans:
    print(*k)
