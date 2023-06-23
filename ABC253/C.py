from collections import defaultdict
import heapq
Q = int(input())
S_dic = defaultdict(int)
max_S = []
min_S = []

for _ in range(Q):
    que = list(map(int,input().split()))
    if que[0] == 1:
        x = que[1]
        S_dic[x] += 1
        heapq.heappush(max_S, -x) # インデックスが0の時に最大の値がくるようにするためマイナスをつける 
        heapq.heappush(min_S, x)  # インデックスが0の時に最小の値がくるようにするためマイナスをつけない
    elif que[0] == 2:
        x = que[1]
        c = que[2]
        if S_dic[x] > c:
            S_dic[x] -= c
        else:
            S_dic.pop(x)
    else:
        while S_dic[-max_S[0]] == 0: # -max_S[0]としているのは、入っている値がマイナスであるためそのままではインデックス指定に使えないから
            heapq.heappop(max_S)
        while S_dic[min_S[0]] == 0:
            heapq.heappop(min_S)
        print(-max_S[0] - min_S[0])
