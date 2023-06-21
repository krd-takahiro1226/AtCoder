N = int(input())
N_str = str(N)
N_ln = len(N_str)
ans = 0


if N_ln % 2 == 0:
    for i in range(2, N_ln+1,2):
        ans += 9 * 10 ** (i - 2)
else:
    ans = N - 10 ** (N_ln-1) + 1
    for i in range(2, N_ln+1,2):
        ans += 9 * 10 ** (i - 2)
print(ans)
