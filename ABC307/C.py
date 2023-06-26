ha, wa = map(int,input().split())
A = [input() for _ in range(ha)]
hb, wb = map(int,input().split())
B = [input() for _ in range(hb)]
hx, wx = map(int,input().split())
X = [input() for _ in range(hx)]
A_ind = []
B_ind = []
X_ind = []

for i in range(ha):
    for j in range(wa):
        if A[i][j] == "#":
            A_ind.append((i,j))
for i in range(hb):
    for j in range(wb):
        if B[i][j] == "#":
            B_ind.append((i,j))
for i in range(hx):
    for j in range(wx):
        if X[i][j] == "#":
            X_ind.append((i,j))

A_num = len(A_ind)
B_num = len(B_ind)
X_num = len(X_ind)

# print(A_ind)
# print(B_ind)
# print(X_ind)
