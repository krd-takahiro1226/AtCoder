N, K, X = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
A.sort(reverse=True)
A_sum = sum(A)
for i in range(N):
    if K > 0 and A[i] > X:
        use = A[i] // X
        if K > use:
            A[i] = A[i] % X
            K -= use
        else:
            A[i] -= K * X
            K = 0

A.sort(reverse=True)
for j in range(N):
    if K <= 0:
        break
    else:
        A[j] = 0
        K -= 1

print(sum(A))

# 解説を参考に実装したコード(TLEする)
# 制約より、K <= 10**9のため、Kを含んだfor文の最悪計算量が10**9になりTLEする
# if cnt < K:
#     A.sort(reverse=True)
#     for k in range(K-cnt):
#         if k < N:
#             A[k] = 0
#     ans = sum(A)
# else:
#     ans = A_sum - K * X
# print(ans)



# sortが計算負荷高すぎてTLE
# while cnt != K:
#     A[i] = max(A[i]-X ,0)
#     A.sort(reverse=True)
#     cnt += 1

# for j in range(N):
#     ans += A[j]
# print(ans)
