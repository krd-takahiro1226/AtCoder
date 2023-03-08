import copy
N = int(input())
A = list(map(int, input().split()))

A_copy = copy.copy(A)
A_square = list(map(lambda x: x ** 2, A))
A_square_sum = sum(A_square)
score = A_square_sum * (N - 1)
sum_A = sum(A_copy)

ans = [0] * N

for i in range(N):
    minus = A[i] * (sum_A - A[i])
    ans[i] = minus
# print(ans)
print(score - sum(ans))
