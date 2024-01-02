N, M ,P = map(int,input().split())
date = M
ans = 0

while (date <= N):
    date += P
    ans += 1

print(ans)
