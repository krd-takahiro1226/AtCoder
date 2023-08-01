N = input()

if len(N) != 4:
    ans = "0" * (4-len(N)) + N
    print(ans)
else:
    print(N)
