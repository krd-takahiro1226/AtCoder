# from collections import deque
N = int(input())
Q = int(input())
box = [[] for _ in range(N+1)]
cards = [set() for _ in range(2*10**5+1)]
# ↓のように定義し、query[0] == 3の時にsetに変換するとTLEする
# list→setの変換が無駄だし計算負荷高め？ → set(list)の計算量はO(N)だからこの処理の負荷が高い
# cards = [[] for _ in range(2*10**5+1)]


for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        box[query[2]].append(query[1])
        cards[query[1]].add(query[2])
    elif query[0] == 2:
        box_i = box[query[1]]
        box_i.sort()
        print(*box_i)
    elif query[0] == 3:
        boxes = cards[query[1]]
        ans = list(boxes)
        ans.sort()
        print(*ans)











# TLEする
# for _ in range(Q):
#     query = list(map(int,input().split()))
#     if query[0] == 1:
#         box[query[2]-1].append(query[1])
#     elif query[0] == 2:
#         box_i = box[query[1]-1]
#         box_i.sort()
#         print(*box_i)
#     elif query[0] == 3:
#         cnt = 1
#         ans = []
#         # print(box)
#         for box_j in box:
#             # print(box_j)
#             if query[1] in box_j:
#                 ans.append(cnt)
#             cnt += 1
#         print(*ans)
