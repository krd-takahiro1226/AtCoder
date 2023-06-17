N = int(input())
S = list(input())
ans = [0] * (2*N)
shift = 0

for i in range(N):
    ans[i+shift] = S[i]
    ans[i+1+shift] = S[i]
    shift += 1

print(*ans,sep='')
