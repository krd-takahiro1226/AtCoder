A, B = input().split()
A_sum = 0
B_sum = 0
for i in range(3):
    A_sum += int(A[i])
    B_sum += int(B[i])

if A_sum != B_sum:
    print(max(A_sum,B_sum))
else:
    print(A_sum)
