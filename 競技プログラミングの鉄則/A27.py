A, B = map(int,input().split())

while (A != B):
    if A >= B:
        A -= B
    elif A < B:
        B -= A
print(A)

# 解説コード
# ユークリッドの互助法は続けると片方が0になるまで続くからwhileは操作終了まで回る
# 片方が0になる → A = BであるからA >= 1 → Aを出力、そうでなければBを出力(逆はダメ、条件より初めはA >= Bのため、最初のA % B = 0の時、Bが最大公約数に当たるため)
def GCD(A, B):
	while A >= 1 and B >= 1:
		if A >= B:
			A = A % B # A の値を変更する場合
		else:
			B = B % A # B の値を変更する場合
	if A >= 1:
		return A
	return B

# 入力
A, B = map(int, input().split())
print(GCD(A, B))
