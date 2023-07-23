t = int(input())
def ft(t):
    return t**2 + 2*t + 3
ans = ft(ft(ft(t)+t) + ft(ft(t)))
print(ans)
