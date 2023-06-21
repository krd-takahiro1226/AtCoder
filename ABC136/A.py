A, B, C = map(int,input().split())
ans = C - (A - B)

print(max(ans,0))
