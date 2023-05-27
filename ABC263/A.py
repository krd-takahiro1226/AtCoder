A, B, C, D, E = map(int,input().split())
card_list = [A,B,C,D,E]
unique_card = set(card_list)
cnt_list = []
ans = False
# ACしたけど頭悪い
if len(unique_card) == 2:
    for i in unique_card:
        cnt = 0
        for j in card_list:
            if i == j:
                cnt += 1
        if cnt == 2 or cnt == 3:
            cnt_list.append(cnt)

if len(set(cnt_list)) == 2:
    ans = True

if ans:
    print("Yes")
else:
    print("No")
# 別解(辞書で管理)

from collections import defaultdict
dic = defaultdict(int)
for i in card_list:
    dic[i] += 1
dic_sort_list = sorted(dic.values())
if dic_sort_list == [2,3]:
    print("Yes")
else:
    print("No")
