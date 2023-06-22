import copy
N = int(input())
A = [[] for _ in range(N)]
A[0].append(1)
if N >= 2:
    A[1] = copy.deepcopy(A[0])
    A[1].append(1)
    for i in range(1,N-1):
        A[i+1] = copy.deepcopy(A[1])
        for j in range(len(A[i])-1):
            A[i+1].insert(j+1, A[i][j] + A[i][j+1]) 

for ai in A:
    print(*ai)
