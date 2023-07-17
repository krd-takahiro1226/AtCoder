D, N = map(int,input().split())
base = 100 ** D
# このままだとN番目のやつが100で割り切れる可能性を考慮できていない
if N % 100 == 0:
    ans = (N+1) * base
else:
    ans = N * base
print(ans)
