N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
visit = [[] for _ in range(N+1)]
ans = [0] * (N+1)
ans[2] = A[0]

# ゴミカス解答
# for i in range(N-2):
#     visit[i+1].append(ans[i-1] + A[i])
#     visit[i+2].append(ans[i-2] + B[i])
#     ans[i] = min(visit[i+1])
# print(ans)

# 模範解答のコピペ
for j in range(3, N+1):
    ans[j] = min(ans[j-1] + A[j-2], ans[j-2] + B[j-3])
print(ans[N])
