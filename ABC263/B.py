N = int(input())
P = list(map(int,input().split()))
P.insert(0,0)
ans = 1

i = N - 1
while(P[i] != 1):
    ans += 1
    i = P[i] - 1
print(ans)
