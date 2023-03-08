T = int(input())
test_i_len = []
test_case = []
counter = 0
count = 0
ans = [0] * T
for _ in range(2*T):
    counter += 1
    if counter % 2 == 1:
        test_i_len.append(int(input()))
    elif counter % 2 == 0:
        test_case.append(list(map(int, input().split())))

# print("test_i_len",test_i_len)
# print("test_case",test_case)


for length in test_i_len:
    for j in range (length):
        if test_case[count][j] % 2 != 0:
            ans[count] = ans[count] + 1
    count += 1
for l in ans:
    print(l)
