A, B, K = map(int,input().split())
ans = set()

for i in range(K):
    if A+i <= B:
        ans.add(A+i)
    if B-i >= A:
        ans.add(B-i)

ans = list(ans)
ans.sort()
for j in ans:
    print(j)
