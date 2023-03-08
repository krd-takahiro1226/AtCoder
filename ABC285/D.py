import collections
N = int(input())
ST = [list(input().split()) for _ in range(N)]
S = []
T = []
cnt = 0

class UnionFind():
    def __init__(self):
        '''
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        '''
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
    

uf = UnionFind()

# 全ての要素をグラフ化
for i in range(N):
    uf.union(ST[i][0], ST[i][1])


for j in uf.roots():
    for k in uf.all_group_members()[j]:
        if j == k:
            cnt += 1
        else:
            pass

if cnt != N:
    print("Yes")
else:
    print("No")



# これじゃだめ(ループしてるか判定できてないから)
# if len(uf.roots()) != 1:
#     print("Yes")
# else:
#     print("No")

# print(uf.all_group_members())
# print(uf.roots())
# print(uf.group_count())



# 6
# aaa bbb
# zzz xxx
# ccc ddd
# xxx aaa
# bbb ccc
# ddd zzz


# 6
# a b
# b q
# c d
# e g
# g q
# d e


# 7
# a b
# b q
# c d
# e g
# g q
# d e
# c a
