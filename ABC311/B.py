from collections import defaultdict
N ,D = map(int,input().split())
S = [list(input()) for _ in range(N)]
dic = defaultdict(int)
ans = []

for i in range(N):
    for j in range(D):
        if S[i][j] == "o":
            dic[j+1] += 1

dic_N = {key:value for key, value in dic.items() if value == N}
dic_N_key = list(dic_N.keys())
if len(dic_N_key) != 0:
    cnt = 1
else:
    cnt = 0
for k in range(len(dic_N_key)-1):
    if dic_N_key[k+1] - dic_N_key[k] == 1 and cnt == 0:
        cnt += 2
    elif dic_N_key[k+1] - dic_N_key[k] == 1 and cnt != 0:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
ans.append(cnt)

print(max(ans))
