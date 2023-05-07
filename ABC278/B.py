H, M = map(int,input().split())

while (H % 10 >= 6 or (H + M // 10 - H % 10) > 23):
    M += 1
    if M >= 60:
        M = M % 60
        H += 1
    if H >= 24:
        H = H % 24
print(H,M)
