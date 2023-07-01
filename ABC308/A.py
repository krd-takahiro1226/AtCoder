s = list(map(int,input().split()))
ans = True
for i in range(8):
    if s[i] % 25 != 0:
        ans = False
        break
    if s[i] < 100 or s[i] > 675:
        ans = False
        break

for j in range(7):
    if s[j] > s[j+1]:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
