S = list(input())
T = list(input())
tmp_s = []
ind = []
ans = True

for i in range(len(S)):
    if S[i] != T[i]:
        tmp_s.append(S[i])
        ind.append(i)

if len(tmp_s) == 2 and abs(ind[0] - ind[1]) == 1:
    S[ind[0]] = tmp_s[1]
    S[ind[1]] = tmp_s[0]
elif len(tmp_s) == 0:
    pass
else:
    ans = False

if S == T and ans:
    print('Yes')
else:
    print('No')
