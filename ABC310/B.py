N, M = map(int,input().split())
P = []
C = []
F = []
for _ in range(N):
    PCF = list(map(int,input().split()))
    P.append(PCF[0])
    C.append(PCF[1])
    F.append(set(PCF[2:]))

ans = False
# 超集合(集合2の要素がすべて集合1に含まれているかどうかを判定)を取得するにはissupersetを使う
# 2つ目のfor文の探索範囲を(i,N)にすると、超集合を求めるときにAがBの超集合かしか判定せず、BがAの長集合であるかどうかを考慮できなくなる
# そのため、探索範囲は両方N
for i in range(N):
    for j in range(N):
        if P[i] >= P[j] and F[j].issuperset(F[i]) and (P[i] > P[j] or len(F[i]) < len(F[j])):
            ans = True

print('Yes' if ans else 'No')
