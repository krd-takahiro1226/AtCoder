import bisect
N, Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for _ in range(Q):
    x = int(input())
    ans = N - bisect.bisect_left(A, x)
    print(ans)
