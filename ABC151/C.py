N, M = map(int,input().split())
p = []
S = []
for _ in range(M):
    pS = input().split()
    p.append(int(pS[0]))
    S.append(pS[1])
AC = [False] * (N+1)
WA_cnt = [0] * (N+1)
AC_cnt = [0] * (N+1)
AC_list = set()
# 初めてACを出すまでのWAだからACが出なかったら0を出力しないといけない
for i in range(M):
    if p[i] not in AC_list:
        if S[i] == "WA":
            WA_cnt[p[i]] += 1
        else:
            AC_cnt[p[i]] += 1
            AC_list.add(p[i])
            AC[p[i]] = True
for j in range(M):
    if AC[p[j]] == False:
        WA_cnt[p[j]] = 0

AC = sum(AC_cnt)
WA = sum(WA_cnt)
print(AC,WA)



# if AC:
#     print(AC_cnt,WA_cnt)
# else:
#     print(0,0)
