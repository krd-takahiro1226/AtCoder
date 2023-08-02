N = input()
N_ln = len(N)
MOD = 998244353
inv_2 = 499122177
ans = 0
# 余りを求めるときに割ってはいけない→結果が変わるため(割る代わりに逆元をかける)
for i in range(1, N_ln+1):
    if i != N_ln:
        diff = 10**i - 1 - 10**(i-1) + 1
        val = ((1+diff) % MOD) * (diff % MOD) * inv_2
        ans += val % MOD
    else:
        diff = int(N) - 10**(i-1) + 1
        val = ((1+diff) % MOD) * (diff % MOD) * inv_2
        ans += val % MOD
print(int(ans) % MOD)
