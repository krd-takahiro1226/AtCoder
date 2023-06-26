N = int(input())
S = [list(input()) for _ in range(N)]
ans = False
cnt = 0

for i in range(N):
    for j in range(N):
        if i!= j:
            cnt = 0
            Si = S[i] + S[j]
            for k in range(len(Si)//2):
                if Si[k] == Si[len(Si)-1-k]:
                    cnt += 1
            if cnt == len(Si)//2:
                ans = True
        # cnt = 0
        # if abs(len(S[i]) - len(S[j])) != 1:
        #     continue
        # else:
        #     while (cnt <= len(S[j])-1):
        #         if S[i][len(S[i])-1-cnt] == S[j][cnt]:
        #             cnt += 1
        #         else:
        #             break
        #     if cnt == len(S[j]):
        #         ans = True
if ans:
    print("Yes")
else:
    print("No")
