S = list(input())
T = list(input())
S_cnt = [0] * len(S)
S_cnt_sum = [0] * len(S_cnt)
T_cnt = [0] * len(T)
T_cnt_sum = [0] * len(T_cnt)
ans = True
s_cnt = 1
t_cnt = 1
s_unique_num = 0
t_unique_num = 0

for i in range(1,len(S)):
    if S[i] == S[i-1]:
        s_cnt += 1
    else:
        S_cnt[s_unique_num] = s_cnt
        s_cnt = 1
        s_unique_num += 1
S_cnt[s_unique_num] = s_cnt

for j in range(1,len(T)):
    if T[j] == T[j-1]:
        t_cnt += 1
    else:
        T_cnt[t_unique_num] = t_cnt
        t_cnt = 1
        t_unique_num += 1
T_cnt[t_unique_num] = t_cnt

for l in range(min(len(S_cnt),len(T_cnt))):
    if l == 0:
        S_cnt_sum[l] = S_cnt[l]
        T_cnt_sum[l] = T_cnt[l]
    else:
        S_cnt_sum[l] = S_cnt_sum[l-1] + S_cnt[l]
        T_cnt_sum[l] = T_cnt_sum[l-1] + T_cnt[l]

for k in range(min(s_unique_num,t_unique_num)+1):
    # if文を複雑に書きすぎて逃している条件があった
    #  S_cnt[k] != T_cnt[k]の時、ans = Falseとなるのはどちらかが1でどちらかが1でない時で良い
    # または↓のif文
    if S_cnt[k] != T_cnt[k] and (S_cnt[k] < 2 or T_cnt[k] < S_cnt[k]):
        ans = False
        break
    if S[S_cnt_sum[k]-1] != T[T_cnt_sum[k]-1]:
        ans = False
        break
    if s_unique_num != t_unique_num:
        ans = False
        break
    # if T_cnt[k] < S_cnt[k]:
    #     ans = False
    #     break
    # if (S_cnt[k] != 1 and T_cnt[k] == 1) or (S_cnt[k] == 1 and T_cnt[k] != 1):
    #     ans = False
    #     break
    # ↑この条件をまとめたif文が↓
    # if S_cnt[k] != T_cnt[k] and (S_cnt[k] < 2 or T_cnt[k] < S_cnt[k]):
    #     ans = False
    #     break
if ans:
    print("Yes")
else:
    print("No")


# レングレス圧縮を利用した方法
# def rle(s):
#     n = len(s) #文字列の長さ
#     ans = [] #圧縮後のリスト
#     l = 0 #始点
#     while l<n:
#         r = l+1
#         while r<n and s[l]==s[r]: #異なる文字になるまで進む
#             r += 1
#         ans.append((s[l], r-l)) #文字,連続する個数
#         l = r #連続しなかった文字から探索を開始
#     return ans

# rle_S = rle(S)
# rle_T = rle(T)


# if len(rle_S) != len(rle_T):
#     ans = False

# for i in range(len(rle_S)):
#     if rle_S[i][0] != rle_T[i][0]:
#         ans = False
#         break
#     if (rle_S[i][1] == 1 and rle_T[i][1] != 1) or (rle_S[i][1] != 1 and rle_T[i][1] == 1):
#         ans = False
#         break
#     if rle_T[i][1] < rle_S[i][1]:
#         ans = False
#         break

# if ans:
#     print("Yes")
# else:
#     print("No")
