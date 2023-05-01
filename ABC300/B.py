H, W = map(int,input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]
ans = "No"


# 横が揃っても縦が揃わない可能性があるから4重の全探索をしないといけない。
# i,jはそれぞれ縦と横のシフト幅を表す。
# ある(i,j)のシフト幅の組み合わせにおいて、シフト後の全ての座標が目標行列(B)と一致したらYesを出力
# 3重目と4重目のforはAの全ての座標について、ある(i,j)の分だけシフトさせたものがBと一致したらcntに1追加
# 3重目と4重目のforが回り切った段階でcntの合計がH*Wになっていたら、Aの全ての座標に関してある(i,j)の分シフトすると、Bと一致したことになるため、ans="Yes"
# そうでなければcntを初期化して違う(i,j)の組み合わせを試す。
# ACした人のコード
for i in range(H):
    for j in range(W):
        cnt = 0
        for s in range(H):
            for t in range(W):
                if A[(i+s) % H][(j+t) % W] == B[s][t]:
                    cnt += 1
        if cnt == W*H:
            ans = "Yes"
print(ans)

# 自分が考えたの(間違っている)
# ans_cnt = 0
# for i in range(H):
#     for j in range(W):
#         cnt = 0
#         for s in range(H):
#             for t in range(W):
#                 if A[(s+i) % H][(t+j) % W] == B[s][t]:
#                     cnt += 1
#         if cnt == W*H:
#             ans_cnt += 1
# print(ans_cnt)
# if ans_cnt == H*W:
#     print("Yes")
# else:
#     print("No")
