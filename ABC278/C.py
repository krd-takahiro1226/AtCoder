from collections import defaultdict
N, Q = map(int,input().split())
ff = defaultdict(set)
# ff = [set() for _ in range(N+1)]

for _ in range(Q):
    T, A, B = map(int,input().split())
    if T == 1:
        if B not in ff[A]:
            ff[A].add(B)
    elif T == 2:
        if B in ff[A]:
            ff[A].discard(B)
    else:
        if B in ff[A] and A in ff[B]:
            print("Yes")
        else:
            print("No")
