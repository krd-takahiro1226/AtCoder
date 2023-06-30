from collections import defaultdict
N = int(input())
dic = defaultdict(list)
ans = []


for k in range(N):
    S = list(input())
    for i in range(10):
        si = int(S[i])
        if i not in dic[si]:
            dic[si].append(i)
        else:
            tmp = []
            for j in range(k):
                if i + j*10 in dic[si]:
                    tmp.append(10 + i + j*10)
            for g in tmp:
                dic[si].append(g)

for l in range(10):
    ans.append(max(dic[l]))
print(min(ans))
