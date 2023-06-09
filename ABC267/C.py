N, M = map(int,input().split())
A = list(map(int,input().split()))
A_sum_list = [0] * (N+1)
A_sum_list_index = [0] * (N+1)
B = [0] * (N-M+1)
ans = []
cnt = 0

# Biの数列に関する漸化式を立て、関係性を把握
for i in range(1,N+1):
    A_sum_list[i] = A_sum_list[i-1] + A[i-1]
    A_sum_list_index[i] = A_sum_list_index[i-1] + i*A[i-1]
A_sum_1 = A_sum_list_index[M]
B[0] = A_sum_1

for j in range(1,N-M+1):
    B[j] = B[j-1] + M * A[M+j-1] - (A_sum_list[M+j-1] - A_sum_list[j-1])
    diff = M * A[M+j-1] - (A_sum_list[M+j] - A_sum_list[j])
ans = max(B)
print(ans)











# TLEしそう→した
# for j in range(N-M+1):
#     Ai_sum = 0
#     Ai = A[cnt:M+cnt]
#     for k in range(len(Ai)):
#         Ai_sum += Ai[k] * (k+1)
#     ans.append(Ai_sum)
#     cnt += 1
# print(max(ans))
