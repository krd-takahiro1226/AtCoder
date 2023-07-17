N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0

# 後ろから数えていきそう？
for i in reversed(range(N)):
# i+1番目に対する処理
    if B[i] >= A[i+1]:
        ans += A[i+1]
        B[i] -= A[i+1]
        A[i+1] = 0
    else:
        ans += B[i]
        A[i+1] -= B[i]
        B[i] = 0
# i番目に対する処理
    if B[i] >= A[i]:
        ans += A[i]
        B[i] -= A[i]
        A[i] = 0
    else:
        ans += B[i]
        A[i] -= B[i]
        B[i] = 0

print(ans)
