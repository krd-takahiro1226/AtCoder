N, Q = map(int, input().split())
A = [list(map(int, input().split())) for l in range(N)]
B = [list(map(int, input().split())) for l in range(Q)]

L = [0] * N
a = []
s = [0] * Q
t = [0] * Q

for i in range(N):
    L[i] = A[i][0]
    a.append(list(A[i][1:]))

for j in range(Q):
    s[j] = B[j][0]
    t[j] = B[j][1]
# print(s)
# print(t)

for i in range(Q):
    a_s = a[s[i] - 1]
    a_s_val = a_s[t[i] - 1]
    print(a_s_val)
