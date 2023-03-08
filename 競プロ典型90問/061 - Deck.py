Q = int(input())
tx = [list(map(int, input().split())) for l in range(Q)]
deck = []
ans = []

# print(tx)
for i in range(Q):
    if tx[i][0] == 1:
        deck.insert(0, tx[i][1])
    elif tx[i][0] == 2:
        deck.append(tx[i][1])
    elif tx[i][0] == 3:
        ans.append(deck[tx[i][1] - 1])
    pass

# print(ans)
for j in ans:
    print(j)
