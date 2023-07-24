import bisect
N, K = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(N)]
sum_list = []

# bisectってsortが降順だと機能しない？
for i in range(N):
    sum_list.append(sum(P[i]))
sum_list_sort = sorted(sum_list)
sum_list_ln = len(sum_list)

for j in sum_list:
    ind = sum_list_ln - bisect.bisect_right(sum_list_sort, j+300) + 1
    if ind <= K:
        print('Yes')
    else:
        print('No')
