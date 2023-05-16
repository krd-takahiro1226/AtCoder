H, W = map(int,input().split())
for _ in range(H):
    A = map(int,input().split())
    Si = []
    for i in A:
        if i == 0:
            Si.append(".")
        else:
            Si.append(chr(i+64))
    print(*Si, sep='')
