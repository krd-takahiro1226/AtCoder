X, Y, N = map(int,input().split())
ans_1_main = N * X
num_3 = N // 3
N -= num_3 * 3
ans_3_main = num_3 * Y + N * X
print(min(ans_1_main,ans_3_main))
