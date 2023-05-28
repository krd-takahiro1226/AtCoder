sx,sy,gx,gy = map(int,input().split())

# if gx > sx:
#     ans = (gx * sy + gy * sx)/(sy+gy)
# else:
#     ans = (gx * sy + gy * sx)/(sy+gy)
ans = (gx * sy + gy * sx)/(sy+gy)
print(ans)
