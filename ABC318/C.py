N, D, P = map(int,input().split())
F = list(map(int,input().split()))
F.sort(reverse=True)

cnt = 1
ans = 0

for i in range(0,N,D):
    slice = cnt * D
    eval = F[i:slice]
    if sum(eval) >= P:
        ans += P
        cnt += 1
    else:
        ans += sum(F[i:])
        break
print(ans)
