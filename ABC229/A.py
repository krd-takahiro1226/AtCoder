S = [list(input()) for _ in range(2)]
x_uniq = set()
y_uniq = set()

for i in range(2):
    for j in range(2):
        if S[i][j] == "#":
            if i not in y_uniq and j not in x_uniq:
                ans = False
            else:
                ans = True
            x_uniq.add(j)
            y_uniq.add(i)

print('Yes' if ans else 'No')
