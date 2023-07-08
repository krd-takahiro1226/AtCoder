N = int(input())
A = [list(input()) for _ in range(N)]
B = [[0] * N for _ in range(N)]


for i in range(N):
    for j in range(N):
        if i == 0:
            if  0 < j:
                B[i][j] = A[i][j-1]
        elif i == N-1:
            if j < N-1:
                B[i][j] = A[i][j+1]
        elif j == 0:
            if i < N-1:
                B[i][j] = A[i+1][j]
        elif j == N-1:
            if 0 < i:
                B[i][j] = A[i-1][j]
        else:
            B[i][j] = A[i][j]
B[0][0] = A[1][0]
B[N-1][N-1] = A[N-2][N-1]
for k in B:
    print(*k,sep='')
# print(B)
