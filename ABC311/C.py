# from collections import defaultdict
# import sys
# sys.setrecursionlimit(1000000)
# N = int(input())
# A = list(map(int,input().split()))
# dfs = [[] for _ in range(N)]
# dic = defaultdict(list)
# for i in range(N):
#     dic[i].append(A[i])
# ans_list = []

# # 深さ優先探索を行う関数（pos は現在位置、visited[x] は頂点 x が青色かどうかを表す真偽値）
# # DFSだとTLEする(多分考え方は合っている)
# def dfs(pos, G, visited, ans):
#     visited[pos-1] = True
#     ans.append(pos)
#     for i in G[pos-1]:
#         if visited[i-1] == False:
#             dfs(i, G, visited, ans)
#         else:
#             if i == ans[0]:
#                 ans_list.append(ans)
#                 break

# for j in A:
#     visited = [False] * N
#     dfs(j, dic, visited, ans = [])
#     if len(ans_list) != 0:
#         break

# print(len(ans_list[0]))
# print(*ans_list[0])


# 閉路が見つかった場所から探索する関数
# 開始位置と同じ場所に行き着いたら閉路完成→結果を出力
def getCycle(A, n):
    paths = []
    s = n
    while True:
        paths.append(s)
        s = A[s]
        if s == n:
            return len(paths), paths

N = int(input())
# 要素の値をインデックスに使用したいから-1
A = list(map(lambda x:int(x)-1,input().split()))
visited = [False] * N

n = 0
# Aの1要素目から注目して見ている→whileが止まる=探索済みの所に行き着く=閉路が存在
# 閉路が見つかった座標から探索開始
while not visited[n]:
    visited[n] = True
    n = A[n]
ln, paths = getCycle(A,n)

print(ln)
print(*[x+1 for x in paths])
