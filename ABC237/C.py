S = input()
S_ln = len(S)
ans = False
cnt_f = 0
cnt_b = 0

for i in S:
    if i == "a":
        cnt_f += 1
    else:
        break

for j in range(S_ln):
    if S[S_ln-j-1] == "a":
        cnt_b += 1
    else:
        break

if cnt_b >= cnt_f:
# わざわざforぶん回していたからTLEした→下の記述に変更したことで数倍速くなった
    # for k in range(1,cnt_b-cnt_f+1):
    #     S = "a" + S
    #     if S == S[::-1]:
    #         ans = True
    #         break
    add_str = "a" * (cnt_b - cnt_f)
    S = add_str + S
    if S == S[::-1]:
        ans = True

if ans:
    print('Yes')
else:
    print('No')
