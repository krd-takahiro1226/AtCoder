N = int(input())
S = []
for _ in range(N):
    S.append(input())
name_list = set()
count_list = set()
counter = 0

for i in S:
    counter += 1
    if i in name_list:
        pass # passとcontinueの違いでミスしてるわけではない
    else:
        name_list.add(i)
        count_list.add(counter)
        # print(count_list)
count_list = list(count_list)
count_list.sort()
for j in count_list:
    print(j)


# 解説のやり方
# n = int(input())
# set_ = set()

# for i in range(1, n+1):
#     s = input()
#     if s in set_:
#         continue
#     set_.add(s)
#     print(i)




# 計算量減らすため重複要素の探索を減らそうとしたやつ(本質はここではなかった)
# S_dup = sorted(set(S), key=S.index)
# for i in S_dup:
#     count_list.append(S.index(i) + 1)
# count_list.sort()
# for j in count_list:
#     print(j)

# 自力では無理なので答え見る
# for i in S:
#     counter += 1
#     if i in name_list:
#         pass
#     else:
#         name_list.append(i)
#         count_list.append(counter)


# 15
# e869120
# atcoder
# e869120
# square1001
# square1001
# square1002
# faoooa
# ejojod
# aojojo
# atcoder
# hoahohdoa
# aohoaho
# zzzz
# 11111
# zzzz
