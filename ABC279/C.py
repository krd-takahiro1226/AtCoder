H, W = map(int,input().split())
S = []
T = []
S_shift =[[] for _ in range(W)]
T_shift =[[] for _ in range(W)]

# sortすると一定の規則で並び替えられる→2つをsortして完全一致したら入れ替え可能と判定できる
# 多重集合(setの重複許可版？)を使用する

for _ in range(H):
    S.append(list(input()))
for _ in range(H):
    T.append(list(input()))

for i in range(H):
    for j in range(W):
        S_shift[j].append(S[i][j])
        T_shift[j].append(T[i][j])

S_shift.sort()
T_shift.sort()
if S_shift == T_shift:
    print("Yes")
else:
    print("No")
