N = int(input())
a = list(map(int,input().split()))
d = []
num = []
top = 0

# 何で詰まっていたのか→消した後、先頭のやつが何回連続しているかを保持できていなかった
# numで何回連続しているかを保持
# dで消えること含めてのリストを保持
for i in a:
    d.append(i)
# 先頭と同じでなかったらnumに新しく1を追加(1個入るから1)
# cntに1足すのは、要素数が増えるから→cntとpop_cnt消して(len(num))でもよかったかも→修正
    if i != top:
        num.append(1)
    else:
        num[len(num)-1] += 1
    if num[len(num)-1] == i:
        for _ in range(i):
            d.pop()
        num.pop()
    if len(d) >= 1:
        top = d[len(d)-1]
    else:
        top = 0
    print(len(d))
