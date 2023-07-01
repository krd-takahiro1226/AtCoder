from collections import defaultdict
from decimal import Decimal
N = int(input())
# dic = defaultdict(list)
dic = defaultdict(int)
cnt = 1
ans = []
# Decimalを使用すると、不動小数点の計算を正確にできるため、丸め誤差によるミスがなくなる
for _ in range(N):
    A, B = map(Decimal,input().split())
    prob = A / (A+B)
    # dic[prob].append(cnt)
    dic[cnt] = prob
    cnt += 1

dic_sort = sorted(dic.items(),key=lambda x:x[1],reverse=True)
dic_sort = dict((x,y) for x,y in dic_sort)
# print(dic_sort)

for keys in dic_sort.keys():
    ans.append(keys)
print(*ans)




# for key in dic.keys():
#     dic[key].sort()
# dic_sort = sorted(dic.items(),reverse=True)
# dic_sort = dict((x,y) for x,y in dic_sort)
# for value in dic_sort.values():
#     for k in value:
#         ans.append(k)

# print(*ans)
