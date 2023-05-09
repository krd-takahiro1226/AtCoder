N = int(input())
city_name = []
city_pop = []
cnt = 0
ans = None
for _ in range(N):
    S, P = input().split()
    P = int(P)
    city_name.append(S)
    city_pop.append(P)
pop_sum = sum(city_pop)
pop_sum_half = pop_sum // 2 + 1
for i in city_pop:
    if i >= pop_sum_half:
        ans = city_name[cnt]
    cnt += 1
if ans == None:
    ans = "atcoder"
print(ans)
