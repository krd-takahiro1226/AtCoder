N = int(input())
S = list(input())
T = []
ans = True
for i in range(N//2):
    T.append(S[i])

if T + T != S:
    ans = False

print('Yes' if ans else 'No')
