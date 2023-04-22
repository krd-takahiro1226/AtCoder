N = int(input())
S = list(input())
ans = 0
cnt = 1
cnt_s = 0
result = []
TF = False

for i in S:
    if i == "o":
        ans += 1
    elif i == "-":
        result.append(ans)
        ans = 0
    if cnt == N:
        result.append(ans)
    cnt += 1

# print(result)
if len(result) >= 1:
    if max(result) != 0:
        TF = True

if TF == False or "-" not in S:
    print(-1)
else:
    print(max(result))
