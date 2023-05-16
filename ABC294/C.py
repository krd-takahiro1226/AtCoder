import bisect
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = A + B
C.sort()
ans_A = []
ans_B = []
for i in A:
    ind = bisect.bisect_right(C,i)
    ans_A.append(ind)
for j in B:
    ind = bisect.bisect_right(C,j)
    ans_B.append(ind)

print(*ans_A)
print(*ans_B)
