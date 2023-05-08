S = list(input())
T = list(input())
ans = 1

for i in range(len(S)):
    if T[i] == S[i]:
        ans += 1
    else:
        break
print(ans)
