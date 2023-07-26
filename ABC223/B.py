S = input()
ans = []

for i in range(len(S)):
    T = S[i:len(S)] + S[:i]
    ans.append(T)

print(min(ans))
print(max(ans))
