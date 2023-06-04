N , A, B = map(int,input().split())
S = list(input())
j_cnt = 0 
# 一致していない箇所の数を格納
# 1要素目はシフト0
cnt_list = []
value_list = []

for shift in range(N//2 + 1):
    cnt = 0
    for i in range(N//2):
        if S[(i+shift)%N] != S[(N-i-1+shift)%N]:
            cnt += 1
    cnt_list.append(cnt)
# print(cnt_list)

for j in cnt_list:
    value = 0
    value += j * B + j_cnt * A
    j_cnt += 1
    value_list.append(value)

print(min(value_list))
