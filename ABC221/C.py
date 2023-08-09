import itertools
N = list(input())
N_ln = len(N)
N_all = list(itertools.permutations(N))
ans = 0

for pro in N_all:
    shift = 1
    while (N_ln // 2 + 1 != shift):
        N_left = pro[:shift]
        N_right = pro[shift:]
        if N_left[0] != "0" and N_right[0] != "0":
            N_left = int("".join(N_left))
            N_right = int("".join(N_right))
            val = N_left * N_right
            if val > ans:
                ans = val
        shift += 1

print(ans)
