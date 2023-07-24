S, T, X = map(int,input().split())

if S <= X <= T:
    ans = True
elif S > T:
    if T <= X < S:
        ans = False
    else:
        ans = True
else:
    ans = False

print('Yes' if ans else 'No')
