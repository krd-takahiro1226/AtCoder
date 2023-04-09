import math
N, X = map(int,input().split())
A = list(map(int,input().split()))
L = 0
R = len(A)
M = (L + R) // 2
iteration = int(math.log2(N)) + 1
for _ in range(iteration):
# while (L <= R):
    if A[M] > X:
        R = M - 1
        M = (L + R) // 2
    elif A[M] < X:
        L = M + 1
        M = (L + R) // 2
    else:
        break
print(M+1)
