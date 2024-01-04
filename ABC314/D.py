N = int(input())
S = input()
Q = int(input())
txc = [list(input().split()) for _ in range(Q)]
S_list = list(S)
ans = []
cnt = 0
last_ind = 10 ** 9

for i in range(Q):
    t = int(txc[i][0])
    x = int(txc[i][1])
    c = txc[i][2]
    if t == 2 or t == 3:
        last_ind = cnt
    cnt += 1

for j in range(Q):
    t = int(txc[j][0])
    x = int(txc[j][1])
    c = txc[j][2]
    if t == 1 and j >= last_ind:
        ans[x-1] = c
    elif t == 1:
        S_list[x-1] = c
    elif t == 2 and j == last_ind:
        for k in S_list:
            ans.append(k.lower())
    elif t == 3 and j == last_ind:
        for k in S_list:
            ans.append(k.upper())

if len(ans) == 0:
    ans = S_list
print(*ans,sep="")
