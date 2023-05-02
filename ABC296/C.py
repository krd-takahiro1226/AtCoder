N, X = map(int,input().split())
A = list(map(int,input().split()))
A_unique = set(A)
ans = False

for i in range(N):
    if A[i] + X in A_unique or A[i] - X in A_unique:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")





# dp = [[] for _ in range(N+1)]
# diff = [0] * N
# diff_sum = [0] * N
# A.sort()
# print(A)
# for i in range(N-1):
#     diff[i+1] = A[i+1] - A[i]
# print(diff)

# for i in range(N-1):
#     diff_sum[i+1] = diff_sum[i] + diff[i+1]
# print(diff_sum)

# diff_sum_unique = set(diff_sum)

# if X in diff_sum_unique:
#     print("Yes")
# else:
#     print("No")
