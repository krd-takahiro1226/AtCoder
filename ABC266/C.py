from itertools import product
import math
ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
dx,dy = map(int,input().split())
a = [ax,ay]
b = [bx,by]
c = [cx,cy]
d = [dx,dy]
point_list = [a,b,c,d]
degree_list = [[b,d],[a,c],[b,d],[c,a]]
theta_list = []
ans = True

def vec_size(vec):
    return math.sqrt(vec[0] ** 2 + vec[1] ** 2)

def vec_inner(vec_1,vec_2):
    return vec_1[0] * vec_2[0] + vec_1[1] * vec_2[1]

for i in range(4):
    standard = point_list[i]
    other_point = degree_list[i]
    vec_1 = [other_point[0][0]-standard[0],other_point[0][1]-standard[1]]
    vec_2 = [other_point[1][0]-standard[0],other_point[1][1]-standard[1]]
    vec_1_size = vec_size(vec_1)
    vec_2_size = vec_size(vec_2)
    inner = vec_inner(vec_1,vec_2)
    cos_theta = inner / (vec_1_size * vec_2_size)
    theta = math.degrees(math.acos(cos_theta))
    theta_list.append(theta)

# theta_sumが少数のため、四捨五入を行う必要あり
theta_sum = round(sum(theta_list),2)
if int(theta_sum) != 360:
    ans = False

if ans:
    print("Yes")
else:
    print("No")
