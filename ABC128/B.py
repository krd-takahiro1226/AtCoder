# N = int(input())
# SP = [list(input().split()) for _ in range(N)]
# city = set()
# for i in range(N):
#     city.add(SP[i][0])
# city = list(city)
# city.sort()
# ans = []
# for j in city:
#     cnt = 1
#     ans_i = []
#     for k in SP:
#         if k[0] == j:
#             ans_i.append([int(k[1]),cnt])
#         cnt += 1
#     ans_i.sort(reverse=True)
#     for l in ans_i:
#         ans.append(l[1])

# for g in ans:
#     print(g)


# 別解
# 100-valueをすることで、評価の昇順降順を入れ替えている→s.sort()で一発で入れ替えできるようになる
n = int(input())
s = []
for i in range(1, n + 1):
    tmp = list(input().split())
    tmp.append(i)
    tmp[1] = 100 - int(tmp[1])
    s.append(tmp)

s.sort()

for x in s:
    print(x[2])
