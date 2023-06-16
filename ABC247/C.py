import copy
N = int(input())
S = [0] * (1+2*(N-1))
Si = [1]
S_prev = [1]

for i in range(N-1):
    Si.extend(S_prev)
    Si.insert(len(S_prev),i+2)
    S_prev = copy.deepcopy(Si)
print(*Si)
