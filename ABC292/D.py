import sys
sys.setrecursionlimit(10**6)
N, M = map(int,input().split())
graph = [[] for _ in range(N)]
connect_label = [0] * N
visited = [False] * N
label_num = 0
side_cnt_list = []
top_cnt_list = []
# グラフの受け取り
for _ in range(M):
    i, j = map(int,input().split())
    graph[i - 1].append(j)
    graph[j - 1].append(i)

# 深さ優先探索
def DFS(i):
    visited[i] = True
    for j in graph[i]:
        if visited[j - 1] == True:
            connect_label[j - 1] = label_num
            continue
        DFS(j - 1)

for i in range(N):
    if visited[i] == True:
        connect_label[i] = label_num
        continue
    else:
        label_num += 1
        DFS(i)

if 0 in connect_label:
    print("No")
else:
    for j in range(1, label_num + 1):
        side_cnt = 0
        label_ind = 0
        top_cnt = 0
        for k in connect_label:
            if k == j:
                side_cnt += len(graph[label_ind])/2
                top_cnt += 1
            label_ind += 1
        side_cnt_list.append(int(side_cnt))
        top_cnt_list.append(top_cnt)
    if side_cnt_list == top_cnt_list and side_cnt_list and top_cnt_list:
        print("Yes")
    else:
        print("No")
