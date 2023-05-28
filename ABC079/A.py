N = input()
cnt_1 = 0
cnt_2 = 0

for i in range(3):
    if N[i] == N[i+1] == N[0]:
        cnt_1 += 1

for i in range(3):
    if N[i] == N[i+1] == N[3]:
        cnt_2 += 1

if cnt_1 >= 2 or cnt_2 >= 2:
    print("Yes")
else:
    print("No")
