N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum = 0
for i in B:
    sum += A[i - 1]

print(sum)
