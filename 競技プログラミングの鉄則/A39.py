N = int(input())
movie_end_start = []
for _ in range(N):
    l, r = map(int,input().split())
    movie_end_start.append([r, l])
movie_end_start.sort()
ans = 0

# 貪欲法(毎回ベストな選択をとり続ける)に則って考える
# 貪欲法の戦略としては、終了時刻が早い映画を選び続ける戦略を取る
# 終了時刻が早い順にソート、上から映画を見れるなら見る、見れないなら次に行くを繰り返す
for i in range(N):
    start = movie_end_start[i][1]
    end = movie_end_start[i][0]
    if i != 0:
        if start < end_tmp:
            pass
        else:   # elif end_tmp <= start:
            ans += 1
            start_tmp = start
            end_tmp = end
    else:
        ans += 1
        start_tmp = start
        end_tmp = end

print(ans)

# 自分で考えたコード(ほとんどTLEする、WAもあり)
# 被っていない時間帯に映画を入れていく(映画の数はcntに保存)
# for i in range(N):
#     L_i = LR[i][0]
#     R_i = LR[i][1]
#     for j in range(L_i+1, R_i):
#         if ans_list[j] == 0:
#             ans_list[j] = cnt
#     cnt += 1
# ans_unique = list(set(ans_list))
# for k in ans_unique:
#     if k > 0:
#         ans += 1
# print(ans)
