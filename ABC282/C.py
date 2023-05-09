N = int(input())
S = list(input())
i = 0
cnt = 0
while (i < N):
    if S[i] == '"':
        cnt += 1
    if cnt % 2 == 0 and S[i] == ",":
        S[i] = "."
    i += 1
print(*S,sep='')
