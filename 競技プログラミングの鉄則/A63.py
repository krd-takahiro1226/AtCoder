import sys
from collections import deque
sys.setrecursionlimit(100000)
N , M = map(int,input().split())
graph = [[] for _ in range(N+1)]
# -1で初期化
dist = [-1] * (N+1)
dist[1] = 0
Q = deque()
Q.append(1)

# グラフの受け取り(1オリジン受け取り)
for _ in range(M):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

while len(Q) >= 1:
# 初めは1(スタート地点)
    pos = Q.popleft()
# スタート地点と連結している場所1つ1つに対してfor文を行う
    for i in graph[pos]:
# distに既に値が入ってた場合、-1以外が入っている。dist = -1を満たさない場合は上書きしてしまうから実行しない。
        if dist[i] == -1:
            dist[i] = dist[pos] + 1
            Q.append(i)

for i in range(1,N+1):
    print(dist[i])
