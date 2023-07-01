a, b, c, d, e, f, x = map(int,input().split())
tak_syou = x // (a+c)
tak_amari = x % (a+c)
aoki_syou = x // (d+f)
aoki_amari = x % (d+f)

if tak_amari <= a:
    tak = a * b * (tak_syou) + tak_amari * b
else:
    tak = a * b * (tak_syou) + a * b

if aoki_amari <= d:
    aoki = d * e * (aoki_syou) + aoki_amari * e
else:
    aoki = d * e * (aoki_syou) + d * e

if tak > aoki:
    print("Takahashi")
elif tak == aoki:
    print("Draw")
else:
    print("Aoki")
