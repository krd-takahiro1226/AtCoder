import math
# import sys
A , B , C = map(int, input().split())
# sys.setrecursionlimit(10**1)
cd_max_1 = math.gcd(A , B)
cd_max = math.gcd(cd_max_1 , C)
# cd_max_3 = math.gcd(B , C)
A_cut = int(A // cd_max - 1)
B_cut = int(B // cd_max - 1)
C_cut = int(C // cd_max - 1)

all_cut_num = A_cut + B_cut + C_cut
print(all_cut_num)
# print(type(all_cut_num))
