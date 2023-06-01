N = int(input())
S = []
for _ in range(N):
    S.append(input())
S_unique = set(S)
cnt = 0

for i in S_unique:
    if ("!" + i) in S_unique:
        print(i)
        break
    else:
        cnt += 1

if cnt == len(S_unique):
    print("satisfiable")
