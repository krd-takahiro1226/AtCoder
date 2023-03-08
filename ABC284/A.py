N = int(input())
S = []
for _ in range(N):
    S.append(input())
S_conv = []
for i in range(N):
    # S_conv.append(S[N - i - 1])
    print(S[N - 1 - i])
# print(S_conv)
