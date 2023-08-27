N = int(input())
A = list(map(int,input().split()))
A.sort()
A_min = min(A)
cnt = A_min

for i in range(N):
    if A[i] != cnt:
        print(cnt)
        break
    cnt += 1
