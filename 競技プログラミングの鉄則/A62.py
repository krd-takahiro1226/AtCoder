import sys
sys.setrecursionlimit(100000)
N , M = map(int,input().split())
graph = [[] for _ in range(N)]
ans = True
visited = [False] * N

# グラフの受け取り
for _ in range(M):
    i, j = map(int,input().split())
    graph[i - 1].append(j)
    graph[j - 1].append(i)

# 深さ優先探索(調べたやつ)
def DFS(i):
    visited[i] = True
    for j in graph[i]:
        if visited[j - 1] == True:
            # ans[j - 1] = cnt # ここがメイン処理？
            continue
        DFS(j - 1)

# 深さ優先探索は開始位置から連結している部分全てを回っていく探索手法
#  → 連結かそうでないかを見極めたいのであれば、開始位置を指定してあげて実行 → visitedにFalseがなければ連結と判断することができる
DFS(0)
for i in visited:
    if i == False:
        ans = False
        break
    else:
        ans = True

if ans == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
