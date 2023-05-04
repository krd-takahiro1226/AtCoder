from decimal import Decimal, ROUND_HALF_UP
X, K = map(int,input().split())
cnt = 1

# 四捨五入がroundには対応していない(5をうまく処理できない)から、Decimalを使用
for i in range(K):
    order = "1E"
    order += f"{cnt}"
    X = int(Decimal(str(X)).quantize(Decimal(order), rounding=ROUND_HALF_UP))
    cnt += 1
print(X)

# ACしたけどforが一回多く回す必要があったコード
# K+1回forを回さないと試行回数が確保できない？
# Decimalの理解が間違っていた → order = 0の時が不要なのに回してたから余分に一回回す必要があった。
# for i in range(K+1):
#     if i == 0:
#         order = "0"
#     else:
#         order = "1E"
#         order += f"{cnt}"
#     X = int(Decimal(str(X)).quantize(Decimal(str(order)), rounding=ROUND_HALF_UP))
#     cnt += 1
# print(X)
