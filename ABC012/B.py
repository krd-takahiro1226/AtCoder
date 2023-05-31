N = int(input())
hour_len = False
min_len = False
sec_len = False


hour = N // 3600
if len(str(hour)) == 1:
    hour_str = "0" + str(hour)
else:
    hour_str = str(hour)
N -= hour * 3600
min = N // 60
if len(str(min)) == 1:
    min_str = "0" + str(min)
else:
    min_str = str(min)
N -= min * 60
sec = N
if len(str(sec)) == 1:
    sec_str = "0" + str(sec)
else:
    sec_str = str(sec)


print(hour_str + ":" + min_str + ":" + sec_str)
