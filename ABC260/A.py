S = list(input())
S_unique = set(S)
ans_list = []

for i in S:
    ans_list.append(S.count(i))


if 1 not in ans_list:
    print(-1)
else:
    print(S[ans_list.index(1)])
