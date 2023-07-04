from collections import defaultdict
S = list(input())
dic = defaultdict(int)
ans = ""

for i in range(len(S)):
    dic[S[i]] += 1
dic_sort = sorted(dic.items())

for j in range(len(dic_sort)):
    string = dic_sort[j][0]
    num = dic_sort[j][1]
    for k in range(num):
        ans += string
print(ans)
