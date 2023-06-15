h1, h2, h3, w1, w2, w3 = map(int,input().split())
h = [h1,h2,h3]
w = [w1,w2,w3]
ans_cand_list_row = []
ans_cand_list_line = []
cand =[]
ans = 0
# hの合計とwの合計が等しくなかったら答えは0→足し合わせたかを変えてるだけで合計は変わらないから
# 3列中2列が決まったら残りは勝手に決まることを利用する
# →横を見てあり得る可能性をすべて列挙→その後、すべてのパターンに対して、縦の和を考える
# →縦の和がその列に設定された値から1引いた値以上ならansに1追加(各要素は各要素は正の整数の為)
# 横
for hi in h:
    ans_cand_row = []
    for i in range(1,31):
        for j in range(1,31):
            k = hi - i - j
            if k > 0:
                ans_cand_row.append([i,j,k])
    ans_cand_list_row.append(ans_cand_row)

first_row = ans_cand_list_row[0]
second_row = ans_cand_list_row[1]
third_row = ans_cand_list_row[2]

if sum(h) == sum(w):
    for x in first_row:
        for y in second_row:
            if x[0] + y[0] <= w1 - 1 and x[1] + y[1] <= w2 - 1 and x[2] + y[2] <= w3 - 1:
                ans += 1
    print(ans)
else:
    print(0)
