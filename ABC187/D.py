N = int(input())
A = []
B = []
S = []
S_A = []
ans = 0
value = 0
for _ in range(N):
    Ai,Bi = map(int,input().split())
    A.append(Ai)
    B.append(Bi)
for i in range(N):
    S.append(A[i] + B[i])
for j in range(N):
    S_A.append(S[j] + A[j])

A_sum = sum(A)
S_A.sort(reverse=True)

while (A_sum >= value):
    value += S_A[ans]
    ans += 1
print(ans)
