S = list(input())
string = set()
ans = True
upper = False
lower = False

for i in range(len(S)):
    if S[i] not in string:
        string.add(S[i])
        if S[i].islower():
            lower = True
        elif S[i].isupper():
            upper = True
    else:
        ans = False
        break

if ans and upper and lower:
    print("Yes")
else:
    print("No")
