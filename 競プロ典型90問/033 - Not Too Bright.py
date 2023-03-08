import numpy as np
H , W = map(int, input().split())
light = []
light_i = [0] * W
for i in range(H):
    light.append(light_i)
light = np.array(light)

if H >= 2 and W >= 2:
    for h in range(0, H, 2):
        if h <= H - 1:
            for w in range(0, W, 2):
                if w <= W - 1:
                    light[h][w] = 1
                else:
                    pass
        else:
            pass
else:
    for h in range(H):
        for w in range(W):
            light[h][w] = 1
# print(light)
print(np.count_nonzero(light))
