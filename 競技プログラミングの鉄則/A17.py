N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
visit = [0] * (N+1)
visit[2] = A[0]
ans = []
ans_i = N

# 最小コスト求めるDP
# 0オリジン
for i in range(3, N+1):
    visit[i] = min(visit[i-1] + A[i-2] , visit[i-2] + B[i-3])
# 1オリジン
# for i in range(2, N):
    # visit[i] = min(visit[i-1] + A[i-1] , visit[i-2] + B[i-2])
# print(visit)

# わからないところ/できなかったところ
# なぜforではダメなのか→最初の1が入っていなかった→ループが足りない？
# for文の変数を使用してどこを通過しているか求めようとした→それだと実際は通っていない箇所も含めて全部見る必要がある
# →通過場所のインデックスを示す変数を別で定義する必要あり

# ほぼ解説通り
# for _ in range(N+1):
while True:# 解説
    ans.append(ans_i)
    if ans_i == 1:
        break
    if visit[ans_i] == visit[ans_i-1] + A[ans_i-2]:
        ans_i -= 1
    elif visit[ans_i] == visit[ans_i-2] + B[ans_i-3]:
        ans_i -= 2
ans.sort()
print(len(ans))
print(*ans)

# 自分の解答(間違っている)
# for i in range(2, N):
    # Ai = visit[i-1] + A[i-1]
    # Bi = visit[i-2] + B[i-2]
    # if Ai > Bi:
    #     visit[i] = Bi
    #     ans.append(max(ans) + 2)
    # elif Ai <= Bi and i == 2:
    #     visit[i] = Ai
    #     ans.append(max(ans) + 1)
    # elif max(ans) == N:
    #     break
# print(visit)
