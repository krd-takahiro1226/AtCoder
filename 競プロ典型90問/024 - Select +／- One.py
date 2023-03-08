N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff_abs = []

for i in range(N):
    diff_abs.append(abs(A[i] - B[i]))

A_sum = sum(A)
B_sum = sum(B)
# sum_diff = abs(A_sum - B_sum)
sum_diff = sum(diff_abs)

# 差の大きさとKを比較、差の大きさとKの偶奇が一致しているか判定、両方満たしたらYes、満たさないことがあったらNo
if K >= sum_diff:
    if K % 2 == sum_diff % 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
