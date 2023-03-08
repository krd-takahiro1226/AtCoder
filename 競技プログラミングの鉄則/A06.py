N, Q = map(int,input().split())
A = list(map(int,input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]

cum_sum = [0] * (N+1)

for i in range(N):
    cum_sum[i + 1] = cum_sum[i] + A[i]

for j in range(Q):
    ans = cum_sum[LR[j][1]] - cum_sum[LR[j][0] - 1]
    print(ans)
