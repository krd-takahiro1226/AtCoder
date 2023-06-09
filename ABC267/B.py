S = list(input())
ans = True
fall_list = [False] * len(S)
# fall_listはTrue→倒れている、False→倒れていない

if S[0] != "1":
    for i in range(len(S)):
        if S[i] == "0":
            fall_list[i] = True
    row_list = [[fall_list[6]],[fall_list[3]],[fall_list[1],fall_list[7]],[fall_list[0],fall_list[4]],[fall_list[2],fall_list[8]],[fall_list[5]],[fall_list[9]]]
    # print(row_list)
    for j in range(len(row_list)):
        row_1 = row_list[j]
        if False not in row_1:
            continue
        # 立っているピンが1本以上存在↓
        else:
            for k in range(j,len(row_list)):
                # ↓その間に全て倒れている列がある時
                row_2 = row_list[k]
                if False not in row_2:
                    for l in range(k,len(row_list)):
                        row_3 = row_list[l]
                        if False in row_3:
                            ans = True
                            print("Yes")
                            exit()
                        else:
                            continue
                else:
                    continue
    ans = False
    print("No")
else:
    ans = False
    print("No")
