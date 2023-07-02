a, b, c, d = map(int,input().split())
tak = False
aoki = False

if a > c:
    aoki = True
elif a < c:
    tak = True
else:
    if b > d:
        aoki = True
    elif b <= d:
        tak = True

if tak:
    print("Takahashi")
if aoki:
    print("Aoki")
