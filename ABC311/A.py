N = int(input())
S = list(input())
abc = ["A","B","C"]
abc = set(abc)

for i in range(N):
    if S[i] in abc:
        abc.remove(S[i])
    if len(abc) == 0:
        print(i+1)
        break
