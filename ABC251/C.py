N = int(input())
cnt = 1
sumbit = set()
value = 0

for _ in range(N):
    S,T = input().split()
    T = int(T)
    if S not in sumbit:
        sumbit.add(S)
        if T > value:
            value = T
            ans = cnt
    cnt += 1

print(ans)
