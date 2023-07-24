A, B = input().split()
ans = "Easy"

for i in range(min(len(A),len(B))):
    if int(A[len(A) - i - 1]) + int(B[len(B) - i - 1]) >= 10:
        ans = "Hard"
        break
print(ans)
