X, Y ,Z = map(int,input().split())

if 0 < Y < X:
    if 0 < Z < Y:
        print(abs(X))
    elif Z > Y:
        print(-1)
    else:
        print(abs(Z)*2+X)
elif X < Y < 0:
    if Y < Z < 0:
        print(abs(X))
    elif Y > Z:
        print(-1)
    else:
        print(abs(Z)*2+abs(X))
else:
    print(abs(X))
