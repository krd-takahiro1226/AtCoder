N = int(input())
S = input() 

ans = [0]*(N)
counter = 0


for j in range(N):
    score = 0
    for i in range(N - counter):
        if (i + counter) <= N - 1:
            if S[i] != S[i + counter]:
                score += 1
            else:
                break
        # print(score)
    ans[j] = score
    counter += 1
ans.pop(0)
for i in ans:
    print(i)
# print(ans)


# 7
# adebcgb

# 7
# abadcbb
