N, K, M = map(int,input().split())
A = list(map(int,input().split()))

ideal = N * M
A_sum = sum(A)
diff = A_sum - ideal

if diff > 0:
    print(0)
else:
    if abs(diff) <= K:
        print(abs(diff))
    else:
        print(-1)
