from collections import defaultdict
from bisect import bisect_left
N = int(input())
S = list(input())
W = list(map(int,input().split()))
dic = defaultdict(list)
S_unique = set(S)
ans_list = []
ans = 0

for i in range(N):
    if S[i] == "1":
        dic["adult"].append(W[i])
    else:
        dic["child"].append(W[i])

adult_list = dic["adult"]
child_list = dic["child"]

adult_list.sort()
child_list.sort()

if len(S_unique) == 1:
    print(N)
else:
    for wi in W:
        ans = 0
        adult_score = len(adult_list) - bisect_left(adult_list,wi)
        child_score = bisect_left(child_list,wi)
        ans += adult_score + child_score
        ans_list.append(ans)
    print(max(ans_list))
