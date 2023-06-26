N = int(input())
A = list(map(int,input().split()))
ans = []
value = 0
cnt = 1

for i in range(7*N):
    if cnt % 7 == 0:
        value += A[i]
        ans.append(value)
        value = 0
    else:
        value += A[i]
    cnt += 1
print(*ans)
