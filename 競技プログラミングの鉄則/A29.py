a, b = map(int,input().split())
# a の b 乗を m で割った余りを返す関数
# for文の回る数が30なのはb <= 2 ** 30だから
def Power(a, b, m):
	p = a
	Answer = 1
	for i in range(30):
		wari = 2 ** i
		if (b // wari) % 2 == 1:
			Answer = (Answer * p) % m # a の 2^i 乗が掛けられるとき
		p = (p * p) % m
	return Answer

ans = Power(a,b,10**9+7)
print(ans)
