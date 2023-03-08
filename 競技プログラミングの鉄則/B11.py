import bisect
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
X = [int(input()) for _ in range(Q)]

A.sort()

# C++もライブラリ使用していたのでこれでいいっぽい
for xi in X:
    ind = bisect.bisect_left(A,xi)
    print(ind)
