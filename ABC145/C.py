# import math
# N = int(input())
# xy = [list(map(int,input().split())) for _ in range(N)]
# rslt = [[0] * N for _ in range(N)]
# rslt_sum = 0

# def square(x1,y1,x2,y2):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# # N**2 - Nマスの総和(-Nは対角線状の要素が0だから)をNで割るとN-1マスあたりの値が出る
# # N-1マス当たりの移動距離=1からN番目までの街への移動距離
# for i in range(N):
#     x1 = xy[i][0]
#     y1 = xy[i][1]
#     for j in range(N):
#         x2 = xy[j][0]
#         y2 = xy[j][1]
#         rslt_ij = square(x1,y1,x2,y2)
#         rslt[i][j] = rslt_ij

# for j in rslt:
#     rslt_sum += sum(j)

# print(rslt_sum/N)

# 別解(N!通りを考えるパターン)
import math
from itertools import permutations
def square(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
N = int(input())
xy = [list(map(int,input().split()))for _ in range(N)]
num_list = [i for i in range(N)]
perm_list = list(permutations(num_list))
iter_num = math.factorial(N)
val = 0

for perm in perm_list:
    for j in range(len(perm)-1):
        x1 = xy[perm[j]][0]
        y1 = xy[perm[j]][1]
        x2 = xy[perm[j+1]][0]
        y2 = xy[perm[j+1]][1]
        val += square(x1,y1,x2,y2)

print(val/iter_num)
