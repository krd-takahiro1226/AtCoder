N = int(input())
base_2 = bin(N)
base_2 = base_2.replace("0b","")
cnt = 0
call_list = []
tmp = []

for i in range(len(base_2)-1,-1,-1):
    if i == len(base_2)-1:
        call_list.append(0)
    if base_2[i] == "1":
        for j in range(len(call_list)):
            tmp.append(call_list[j] + 2 ** cnt)
        call_list.append(2 ** cnt)
        for k in tmp:
            call_list.append(k)
        call_list = list(set(call_list))
    cnt += 1
call_list.sort()
for j in call_list:
    print(j)



# 方針は合っていたが実装が間違っていた
# printの順番は昇順に並んでいるべきだが、それが出来ていなかった→appendしてsortが確実
# for i in range(len(base_2)-1,-1,-1):
#     if i == len(base_2)-1:
#         print(0)
#     if base_2[i] == "1":
#         print(2 ** cnt)
#         for j in range(len(call_list)):
#             print(call_list[j] + 2 ** cnt)
#             tmp.append(call_list[j] + 2 ** cnt)
#         call_list.append(2 ** cnt)
#         for k in tmp:
#             call_list.append(k)
#         call_list = list(set(call_list))
#     cnt += 1
