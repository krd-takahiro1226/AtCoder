N, K = map(int,input().split())
A = set(map(int,input().split()))
tmp = 1
result = 0

for i in range(K):
    if i in A and tmp - result == 1:
        result += 1
    else:
        break
    tmp += 1
print(result)

# 全部網羅するっていうやり方がそもそも間違い
# import itertools
# def MEX(Bi, tmp, result):
#     for j in range(len(Bi)):
#         if j in Bi and tmp - result == 1:
#             result += 1
#         else:
#             break
#         tmp += 1
#     return result

# B = set(itertools.combinations(A, K))

# for i in B:
#     ans_cand.append(MEX(i, tmp, result))
# print(max(ans_cand))
