N = int(input())
A = list(map(int,input().split()))
odd_cnt = 0
even_cnt = 0
odd_ind = 0
odd_ind_list = []
even_ind = 0
even_ind_list = []
A.sort()

for i in A:
    if i % 2 == 1:
        odd_cnt += 1
        odd_ind_list.append(odd_ind)
    else:
        even_cnt += 1
        even_ind_list.append(even_ind)
    odd_ind += 1
    even_ind += 1
odd_ind_list.sort()
even_ind_list.sort()

if odd_cnt == 1 and N == 2:
    print(-1)
else:
    if odd_cnt >= 2 and even_cnt >= 2:
        odd_max = A[odd_ind_list[-1]] + A[odd_ind_list[-2]]
        even_max = A[even_ind_list[-1]] + A[even_ind_list[-2]]
        ans = max(odd_max,even_max)
    elif even_cnt >= 2:
        even_max = A[even_ind_list[-1]] + A[even_ind_list[-2]]
        ans = even_max
    elif odd_cnt >= 2:
        odd_max = A[odd_ind_list[-1]] + A[odd_ind_list[-2]]
        ans = odd_max
    print(ans)
