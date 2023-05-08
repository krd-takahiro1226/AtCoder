import collections
N = int(input())
visit = set()
visit.add(1)
# 10**9の長さのリストを作成するとするとメモリエラーでREになる
# Union Findでいける？→いけるけど愚直にやるとTLEする→経路圧縮することで解決(PyPyじゃないとTLEする)

class UnionFind():
    def __init__(self):
        # unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        self.parents = dict()                                      # {子要素:親ID,}
        self.members_set = collections.defaultdict(lambda : set()) # keyが根でvalueが根に属する要素要素(tupleや文字列可)
        self.roots_set = set()                                     # 根の集合(tupleや文字列可)
        self.key_ID = dict()                                       # 各要素にIDを割り振る
        self.ID_key = dict()                                       # IDから要素名を復元する
        self.cnt = 0                                               # IDのカウンター

    def dictf(self,x): # 要素名とIDをやり取りするところ
        if x in self.key_ID:
            return self.key_ID[x]
        else:
            self.cnt += 1
            self.key_ID[x] = self.cnt
            self.parents[x] = self.cnt
            self.ID_key[self.cnt] = x
            self.members_set[x].add(x)
            self.roots_set.add(x)
            return self.key_ID[x]

    def find(self, x):
        ID_x = self.dictf(x)
        if self.parents[x] == ID_x:
            return x
        else:
            self.parents[x] = self.key_ID[self.find(self.ID_key[self.parents[x]])]
            return self.ID_key[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in self.members_set[y]:
            self.members_set[x].add(i)
        self.members_set[y] = set()
        self.roots_set.remove(y)
        self.parents[y] = self.key_ID[x]

    def size(self, x):#xが含まれる集合の要素数
        return len(self.members_set[self.find(x)])

    def same(self, x, y):#同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):#xを含む集合の要素
        return self.members_set[self.find(x)]

    def roots(self):#根の要素
        return self.roots_set

    def group_count(self):#根の数
        return len(self.roots_set)

    def all_group_members(self):#根とその要素
        return {r: self.members_set[r] for r in self.roots_set}

# 頂点数はビルの階層になるからメモリ不足になる
uf = UnionFind()
for _ in range(N):
    A, B = map(int,input().split())
    uf.union(A,B)

UF_list = uf.members(1)
ans = max(UF_list)
print(ans)


# DFSを用いた実装(できていない)
# from collections import defaultdict
# N = int(input())
# graph = defaultdict(list)
# ans = 0
# visited = [False] * (N+1)

# # グラフの受け取り
# for _ in range(N):
#     i, j = map(int,input().split())
#     graph[i].append(j)
#     graph[j].append(i)

# # 深さ優先探索
# def DFS(i,ans):
#     visited[i] = True
#     if i > ans:
#         ans = i
#     for j in graph[i]:
#         if visited[j-1] == True:
#             continue
#         DFS(j,ans)
# DFS(1,ans)
# print(ans)
