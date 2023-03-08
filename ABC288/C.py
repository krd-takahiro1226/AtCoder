N ,M = map(int,input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N)]
graph_ln = []
cnt = 0
ans = [0] * N
visited = [False] * N

for _ in range(M):
    i, j = map(int,input().split())
    graph[i - 1].append(j)
    graph[j - 1].append(i)
print(graph)


# ループしているかどうかを深さ優先探索している
def DFS(i):
    visited[i] = True
    for j in graph[i]:
        if visited[j - 1] == True:
            ans[j - 1] += 1
            continue
        DFS(j - 1)

for i in range(N):
    if visited[i] == True:
        ans[i] += 1
        continue
    else:
        DFS(i)
print(ans)
