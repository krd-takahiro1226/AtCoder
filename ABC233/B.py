L, R = map(int,input().split())
S = input()
sl = S[:L-1]
sr = S[R:]
s_mid = S[L-1:R]
s_mid_re = s_mid[::-1]
ans = sl + s_mid_re + sr
print(ans)
