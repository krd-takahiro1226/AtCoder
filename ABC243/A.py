v, a, b, c = map(int,input().split())
amari = v % (a+b+c)
if amari >= a + b:
    print("T")
elif amari >= a:
    print("M")
else:
    print("F")
