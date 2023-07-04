a, b, c, x = map(int,input().split())
prob = c / (b-a)

if x <= a:
    print(1)
elif x <= b:
    print(prob)
else:
    print(0)
