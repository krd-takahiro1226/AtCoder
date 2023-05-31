N = list(input())
string = N[0]
cnt = 0
for i in range(4):
    if N[i] == string:
        cnt += 1
if cnt == 4:
    print("SAME")
else:
    print("DIFFERENT")
