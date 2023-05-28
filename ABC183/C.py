from itertools import permutations
N, K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]
ans = 0
city_list = [i for i in range(2,N+1)]
add_1 = (1,)

city_perm = list(permutations(city_list))

for pro in city_perm:
    pro = add_1 + pro + add_1
    value = 0
    for j in range(N):
        value += T[pro[j]-1][pro[j+1]-1]
    if value == K:
        ans += 1
print(ans)
