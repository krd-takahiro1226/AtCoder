N , K = map(int,input().split())
S = [input() for _ in range(N)]

S_list = []
for i in range(K):
    S_list.append(S[i])

S_list = sorted(S_list)

for i in S_list:
    print(i)
