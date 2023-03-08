S = input()

score = 0
counter = 1

for i in S:
    score += (ord(i) - 64) * (26**(len(S) - counter))
    counter += 1
print(score)
