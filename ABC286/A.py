N, P, Q, R, S = map(int,input().split())
A = list(map(int,input().split()))
A_copy = A
ans = [0] * N
count_i = 0
count_j = 0

A_i = A[P - 1:Q]
A_j = A[R - 1:S]


for i in range(P-1,Q):
    A[i] = A_j[count_i]
    count_i += 1
for j in range(R - 1, S):
    A[j] = A_i[count_j]
    count_j += 1
print(*A)
