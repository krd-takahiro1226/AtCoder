from collections import defaultdict
N = int(input())
ans = True
st = []
dic = defaultdict(int)

for _ in range(N):
    s,t = input().split()
    st.append([s,t])
    dic[s] += 1
    dic[t] += 1

for i in range(len(st)):
    if st[i][0] != st[i][1]:
        if dic[st[i][0]] >= 2 and dic[st[i][1]] >= 2:
            ans = False
    else:
        if dic[st[i][0]] >= 3 and dic[st[i][1]] >= 3:
            ans = False

if ans:
    print("Yes")
else:
    print("No")

# 1ケースだけ通らなかったやつ→テストケースが複雑で解明不可能
# name = set()
# myouji = set()
# for _ in range(N):
#     s,t = input().split()
    # if s not in myouji and t not in name and t not in myouji and s not in name:
    #     myouji.add(s)
    #     name.add(t)
    #     dic[s] += 1
    #     dic[t] += 1
    # elif s not in myouji and t in name and s not in name:
    #     myouji.add(s)
    #     dic[s] += 1
    # elif s in myouji and t not in name and t not in myouji:
    #     name.add(t)
    #     dic[t] += 1
    # else:
    #     ans = False
