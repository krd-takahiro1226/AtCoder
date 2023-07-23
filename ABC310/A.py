N, P, Q = map(int,input().split())
D = list(map(int,input().split()))

D_min = min(D)
val_1 = P
val_2 = Q + D_min

print(min(val_1,val_2))
