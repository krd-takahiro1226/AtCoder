S = list(input())
S_uniq = set(S)
if len(S_uniq) == 1:
    print(1)
elif len(S_uniq) == 2:
    print(3)
else:
    print(6)
