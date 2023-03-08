import math
N, X = map(int,input().split())
A = list(map(int,input().split()))

L_ind = 1
R_ind = len(A)
search_ind = int((L_ind + R_ind)/ 2) - 1
iteration = int(math.log(N, 2)) + 1 

for i in range(iteration):
    if A[search_ind] < X:
        L_ind = search_ind + 1
        R_ind = R_ind
        search_ind = int((L_ind + R_ind) / 2)
    elif A[search_ind] > X:
        L_ind = L_ind
        R_ind = search_ind - 1
        search_ind = int((L_ind + R_ind) / 2)
    else:
        break

print(search_ind + 1)
