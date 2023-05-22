N = int(input())
A = list(map(int,input().split()))
cnt = 0

for i in range(N-1):
    cnt += abs(A[i+1] - A[i])

for i in range(cnt-1):
    if A[i] >= A[i+1]:
        diff = A[i] - A[i+1]
        while diff != 1:
            A.insert(i+1,A[i]-1)
            diff = A[i] - A[i+1]
    else:
        diff = A[i+1] - A[i]
        while diff != 1:
            A.insert(i+1,A[i]+1)
            diff = A[i+1] - A[i]
print(*A)
