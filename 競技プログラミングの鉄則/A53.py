import queue
import heapq
Q = int(input())
p = []
# 優先度つきキューは、昇順に並んでいるため、インデックスが0の要素が最小となる
# キューに代入する数字を整数として受け取れていなかったから詰まった。

for _ in range(Q):
    query = list(input().split())
    num = int(query[0])
    if num == 1:
        heapq.heappush(p,int(query[1]))
    elif num == 2:
        print(p[0])
    else:
        heapq.heappop(p)
