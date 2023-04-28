import sys
sys.setrecursionlimit(100000)
N , M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
ans = [-1] * (N+1)
cnt = 0
visited = [False] * (N+1)

# 深さ優先探索(調べたやつ)
def DFS(i):
    visited[i] = True
    for j in graph[i]:
        if i > j:
            ans[i] += 1
        if visited[j] == True:
# このcontinueで1つ上のfor文に戻る(意味としては探索済みだから見る必要ないため、次に行く)
            continue
        DFS(j)

DFS(1)

for k in ans:
    if k == 0:
        cnt += 1

print(cnt)


# 昔のコード(解読不能)
# ab = [list(map(int, input().split())) for l in range(M)]
# count = 1
# top_dic = {}
# # 頂点が順番に並んでるとは限らない
# # 一つの頂点に複数の頂点がつながっているときにうまくいかない
# for i in range(M):
#     if ab[i][0] == count:
#         top_dic[count] = ab[i][1]
#     else:
#         pass
#     count += 1
# print(top_dic)
