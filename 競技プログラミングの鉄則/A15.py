# import copy
# N = int(input())
# A = list(map(int,input().split()))
# A_copy = copy.deepcopy(A)
# A.sort()
# A_ind = []
# B = [0] * N
# cnt = 1

# print(A)
# for i in A:
#     A_ind.append(A_copy.index(i))
# print(A_ind)

# for j in A_ind:
#     print(j)
#     B[j] = cnt
#     cnt += 1
# print(B)
# # = の時の処理ができていない

import bisect
N = int(input())
A = list(map(int, input().split()))

T = list(set(A))
T.sort()

B = [ None ] * N
for i in range(N):
	B[i] = bisect.bisect_left(T, A[i])
	B[i] += 1
print(*B)
