import bisect
N = int(input())
A = list(map(int,input().split()))
A_unique = list(set(A))
A_unique.sort()
ans = []

for i in A:
    ind = bisect.bisect_left(A_unique,i) + 1
    ans.append(ind)

print(*ans)
