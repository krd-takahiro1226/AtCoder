import numpy as np
H, W = map(int,input().split()) 
A = [list(map(int, input().split())) for l in range(H)]

B = [[0] * W for i in range(H)]
A_i_sum = []
A_j_sum = []
i_count = 0


for k in range(H):
    A_i_sum.append(sum(A[k]))

for i in range(W):
    A_j = []
    for j in range(H):
        A_j.append(A[j][i])
    A_j_sum.append(sum(A_j))

for i in A_i_sum:
    j_count = 0
    for j in A_j_sum:
        B[i_count][j_count] = i + j
        j_count = j_count + 1
    i_count = i_count + 1

A_np = np.array(A)
B_np = np.array(B)
Ans = B_np - A_np
for a in Ans:
    print(*a)
