S = list(input())
S_ans = ["0"] * 4

for i in range(4):
    if i != 3 and S[i] == "1":
        S_ans[i+1] = "1"
print(*S_ans,sep='')
