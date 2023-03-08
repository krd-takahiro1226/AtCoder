import sys
N ,M = map(int,input().split())
graph = [[] for _ in range(N)]
sys.setrecursionlimit(2000)
graph_ln = []
cnt = 0
ans = [0] * N
visited = [False] * N
# 隣接リスト
for _ in range(M):
    u, v = map(int,input().split())
    graph[u - 1].append(v)
    graph[v - 1].append(u)


def DFS(i):
    visited[i] = True
    for j in graph[i]:
        if visited[j - 1] == True:
            continue
        DFS(j - 1)

for i in range(N):
    if visited[i] == True:
        continue
    else:
        cnt += 1
        DFS(i)
print(cnt)

# 深さが2以上のグラフ構造に対応できていない(そこまで読んで戻るとかができていない)
# for i in range(N):
#     if visited[i] == False:
#         print("通過1")
#         cnt += 1
#         visited[i] = True
#         ans[i] = cnt
#         for j in graph[i]:
#             ans[j - 1] = cnt
#             visited[j - 1] = True
#     else:
#         print("通過2")
#         pass
#     print(visited)
#     print(ans)
# print(max(ans))

# DFSの参考にしたコード
# N, M = map(int, input().split())
# E = [[] for i in range(N)]
# for i in range(M):
#     u, v = map(lambda n: int(n)-1, input().split())
#     E[u].append(v)
#     E[v].append(u)
# ans = 0
# done = set()
# print(E)

# def check_all(v):
#     done.add(v)
#     for u in E[v]:
#         if u in done:
#             continue
#         check_all(u)

# for i in range(N):
#     if i in done:
#         continue
#     else:
#         ans += 1
#         check_all(i)
# print(ans)





# INF = 10**9
# def dfs(v, a, b, c):
#     # N本目までの調査が終わった場合
#     if v == N:
#         # lの最後の要素まで探索して、全ての竹に高さがある場合
#         # 最初、高さ0 => 1本竹を追加する操作は、「合成」ではない。
#         # よってMP = 10 * 3本分の余計なコストを引く
#         if min(a, b, c) > 0:
#             return abs(A - a) + abs(B - b) + abs(C - c) - 30  
#         # lの最後の要素まで探索して、高さ0の竹がある場合
#         else:
#             return INF
#     # メイン部分
#     ret0 = dfs(v + 1, a, b, c)
#     ret1 = dfs(v + 1, a + l[v], b, c) + 10
#     ret2 = dfs(v + 1, a, b + l[v], c) + 10
#     ret3 = dfs(v + 1, a, b, c + l[v]) + 10
#     return min(ret0, ret1, ret2, ret3)


# 5 4
# 1 2
# 1 3
# 3 4
# 4 5


# 5 2
# 1 2
# 1 3


# 7 5
# 1 3
# 1 4
# 3 4
# 3 7
# 5 6


# 5 3
# 1 2
# 3 1
# 4 5
