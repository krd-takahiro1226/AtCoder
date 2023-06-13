K = int(input())

hour = K // 60
K -= 60 * hour
min = K

ans_hour = 21 + hour
ans_min = min

if len(str(ans_min)) == 1:
    ans_min = "0" + str(min)

print(str(ans_hour) + ":" + str(ans_min))
