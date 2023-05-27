N = int(input())
S = list(input())
T = list(input())
ans = True

for i in range(N):
    if S[i] == T[i]:
        pass
    elif S[i] == "1" and T[i] == "l" or T[i] == "1" and S[i] == "l":
        pass
    elif S[i] == "0" and T[i] == "o" or T[i] == "0" and S[i] == "o":
        pass
    else:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
