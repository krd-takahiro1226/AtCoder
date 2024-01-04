from collections import defaultdict
N, M = map(int,input().split())
S = list(input())
C = list(map(int,input().split()))
dic = defaultdict(list)
ans = [False] * (N)
cnt = 1

for i in C:
    dic[i].append(cnt)
    cnt += 1

for keys in dic.keys():
    ln_dic = len(dic[keys])
    for j in range (len(dic[keys])):
        ans[(dic[keys][(j+1) % ln_dic]-1)] = S[(dic[keys][j % ln_dic])-1]
print(*ans,sep='')
