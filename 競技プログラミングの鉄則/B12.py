N = int(input())

L_value = 1
R_value = 100 # N <= 10^6なので、x^3 + x より答えの範囲は100より小さいことがわかる
iteration = 20

def equation_check(x):
    equation = x * (x**2 + 1)
    if equation >= N:
        return True
    elif equation < N:
        return False

for _ in range(iteration):
    search_value = (L_value + R_value) / 2
    if equation_check(search_value) == False:
        L_value = search_value
        R_value = R_value
    elif equation_check(search_value) == True:
        L_value = L_value
        R_value = search_value
print(search_value)
