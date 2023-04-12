S = list(input())
B_ind = [n for n, v in enumerate(S) if v == "B"]
R_ind = [n for n, v in enumerate(S) if v == "R"]
K_ind = [n for n, v in enumerate(S) if v == "K"]

if B_ind[0] % 2 != B_ind[1] % 2 and R_ind[0] < K_ind[0] < R_ind[1]:
    print("Yes")
else:
    print("No")
