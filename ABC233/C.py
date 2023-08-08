# N, X = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(N)]
# l = []
# # 1要素目を追加
# for i in range(a[0][0]):
#     l.append(a[0][i+1])

# for j in range(1,N):
#     l2 = []
#     for k in range(a[j][0]):
#         for g in range(len(l)):
#             l2.append(l[g] * a[j][k+1])
#     l = l2

# print(l.count(X))

# 辞書を使った別解
from collections import defaultdict
N, X = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
l = []
dic = defaultdict(int)
# 1要素目を追加
for i in range(a[0][0]):
    dic[a[0][i+1]] += 1

for j in range(1,N):
    dic2 = defaultdict(int)
    for k in range(a[j][0]):
        val = a[j][k+1]
        for keys, vals in dic.items():
            dic2[keys*val] += vals
# 全ての袋からボールを取り出す → N回試行後の試行後の値にしか興味が無い
# 次の値(積)に関連するのは直前の内容のため、直前の内容を記録しているdic2の値をdicに代入
    dic = dic2
print(dic2[X])


# dpでやろうとしたが、値が大きすぎて記録しきれない
# N, X = map(int,input().split())
# L = []
# a = []
# ln = 10**5
# for _ in range(N):
#     La = list(map(int,input().split()))
#     L.append(La[0])
#     a.append(La[1:])

# dp = [[0] * (ln+1) for _ in range(N)]
# for k in a[0]:
#     dp[0][k] = k

# for i in range(1,N):
#     Li = L[i]
#     for j in range(ln):
#         if dp[i-1][j] != 0:
#             dp[i][j] = dp[i-1][j]
#             for val in a[i]:
#                 if j*val <= ln:
#                     dp[i][j*val] += 1
# print(dp[N-1][X])
