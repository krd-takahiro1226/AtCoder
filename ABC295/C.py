from collections import Counter
N = int(input())
A = list(map(int,input().split()))
A_set = set(A)
A_count = Counter(A)
ans = 0

for i in A_set:
    ans += A_count[i] // 2
print(ans)
