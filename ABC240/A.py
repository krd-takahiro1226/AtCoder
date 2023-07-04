a, b = map(int,input().split())
if abs(b % 10 - a) == 1 or b - a == 1:
    print("Yes")
else:
    print("No")
