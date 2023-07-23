N = int(input())
S = [input() for _ in range(N)]
S_uniq = set(S)

for i in range(N):
    si_rev = S[i][::-1]
    if len(si_rev) > 1 and si_rev in S_uniq:
        S_uniq.remove(si_rev)
        S_uniq.add(S[i])
# print(S_uniq)
print(len(S_uniq))
# print(2*N)
