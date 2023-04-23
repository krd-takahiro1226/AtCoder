N, M ,B = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
sum_A = sum(A)
sum_C = sum(C)

ans = B * M * N + M * sum_A + N * sum_C
print(ans)
