N = int(input())
A = list(map(int,input().split()))
cnt_list = [0] * N
ans = []

for i in range(3*N):
    cnt_list[A[i]-1] += 1
    if cnt_list[A[i]-1] == 2:
        ans.append(A[i])

print(*ans)
