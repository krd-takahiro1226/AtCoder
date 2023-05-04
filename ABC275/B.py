all_list = list(map(int,input().split()))
MOD = 998244353
ABC = 1
DEF = 1
cnt = 1

# 毎処理ごと割るだけでは不十分 → 最後の答えも割る必要がある
for i in all_list:
    if cnt <= 3:
        ABC *= i % MOD
    else:
        DEF *= i % MOD
    cnt += 1

print((ABC - DEF) % MOD)
