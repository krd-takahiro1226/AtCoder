from itertools import combinations
N, W = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
ans = set()

# なんでpythonだと通らない？→計算量10**6だと思うけど
for i in range(1,N+1):
    for j in range(N+1):
        if i != j:
            for k in range(N+1):
                if k != i and k != j or j == k == 0:
                    value = A[i] + A[j] + A[k]
                    if value <= W:
                        ans.add(value)
print(len(ans))
