X, A, D, N = map(int,input().split())

# マイナス同士の割り算の余りはマイナスになるため、絶対値を取ってあげる必要があった
if D != 0:
    if (X - A > 0 and D <= 0) or (X - A < 0 and D >= 0):
        ans = abs(X-A)
        print(ans)
    else:
        syou = abs(X-A)/abs(D)
        if (X-A) % D == 0:
            if syou <= N:
                ans = 0
            else:
                ans = abs(X - (A + (N-1) * D))
        else:
            if syou <= N:
                ans = min(abs(X-A) % abs(D), abs(D) - abs((X-A)) % abs(D))
            else:
                ans = abs(X - (A + (N-1) * D))
        print(ans)
else:
    print(abs(X-A))
