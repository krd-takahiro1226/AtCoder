N, W = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort(reverse=True)
ind = 0
ans = 0

while(W != 0 and ind != N):
    A = AB[ind][0]
    B = AB[ind][1]
    if W > B:
        W -= B
        ans += A*B
    else:
        ans += A*W
        W = 0
    ind += 1
print(ans)
