S = list(input())
cnt = 1
for i in range(len(S)//2):
    ind_1 = cnt * 2 - 2
    ind_2 = cnt * 2 - 1
    tmp_1 = S[ind_1]
    tmp_2 = S[ind_2]
    S[ind_1] = tmp_2
    S[ind_2] = tmp_1
    S_new = S
    cnt += 1
print(*S,sep='')
