N = int(input())
A = [list(map(int,input().split())) for _ in range(2)]
B = [[0] * N for _ in range(2)]
B[0][0] = A[0][0]
B[1][0] = A[0][0] + A[1][0]

for i in range(N-1):
    B[0][i+1] = max(B[0][i] + A[0][i+1], B[0][i+1])
    B[1][i+1] = max(B[1][i] + A[1][i+1], B[0][i+1] + A[1][i+1])
print(B[1][N-1])
