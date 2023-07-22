from collections import defaultdict
N = int(input())
ab = [list(map(int,input().split())) for _ in range(N-1)] 
dic = defaultdict(list)
ans = False

for i in range(N-1):
    dic[ab[i][0]].append(ab[i][1])
    dic[ab[i][1]].append(ab[i][0])

for key, val in dic.items():
    if len(val) == N - 1:
        ans = True

if ans:
    print('Yes')
else:
    print('No')
