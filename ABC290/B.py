N, K = map(int,input().split())
S = input()
win_cnt = 0
cnt = 0
S_ind = []
ans = [0] * N

for i in S:
    if i == "o":
        win_cnt += 1
        S_ind.append(cnt)
    elif i == "x":
        pass
    if win_cnt == K:
        break
    cnt += 1

for j in range(N):
    if j in S_ind:
        ans[j] = "o"
    else:
        ans[j] = "x"

print(*ans,sep = '')
