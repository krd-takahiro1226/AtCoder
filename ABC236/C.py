N, M = map(int,input().split())
S = input().split()
T = input().split()
T_uniq = set(T)

for i in S:
    if i in T_uniq:
        print('Yes')
    else:
        print('No')
