import itertools
import math
import numpy as np
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

# A_iter = list(itertools.combinations(A, 5))
# A_iter = np.array(A_iter)
ans = 0

# for i in A_iter:
#     # if i[0] % P * i[1] % P * i[2] % P * i[3] % P * i[4] % P == Q:
#     #         ans += 1
#     A_i_mod = np.mod(i,P)
#     A_i_prod = math.prod(A_i_mod)
#     if A_i_prod % P == Q:
#         ans += 1
#     else:
#         pass
# print(ans)


for a,b,c,d,e in itertools.combinations(A, 5):
    if a % P * b % P * c % P * d % P * e % P == Q:
        ans += 1
print(ans)

# 6 4 2
# 3 10 1 2 5 7
