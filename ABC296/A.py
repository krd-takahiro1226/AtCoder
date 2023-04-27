N = int(input())
S = list(input())
ans = True

for i in range(N-1):
    if S[i] != S[i+1]:
        pass
    else:
        ans = False
        break
if ans == True:
    print("Yes")
else:
    print("No")
