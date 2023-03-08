A, B = map(int , input().split())

if A + B >= 15 and B >= 8:
    print(1)
elif 10 <= A + B and 3 <= B:
    print(2)
elif 3 <= A + B:
    print(3)
else:
    print(4)
