from itertools import product
from collections import defaultdict
N, K = map(int,input().split())
S = [list(input()) for _ in range(N)]
bit = list(product((0,1),repeat=N))
ans_list = []

for bit_i in bit:
    dic = defaultdict(int)
    ans = 0
    for i in range(len(bit_i)):
        if bit_i[i] == 1:
            s_i = S[i]
            for j in range(len(s_i)):
                dic[s_i[j]] += 1
    for value in dic.values():
        if value == K:
            ans += 1
    ans_list.append(ans)
print(max(ans_list))
