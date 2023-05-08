N = int(input())
S = list(map(int,input().split()))
S.insert(0,0)
ans = [0] * N

for i in range(N):
    ans[i] = S[i+1] - S[i]
print(*ans)
