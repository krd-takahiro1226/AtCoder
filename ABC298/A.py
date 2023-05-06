N = int(input())
S = list(input())

not_good = False
if "x" in S:
    not_good = True
else:
    pass
ok = False
for i in S:
    if i == "o":
        ok = True
    else:
        pass
if not_good == False and ok == True:
    print("Yes")
else:
    print("No")
