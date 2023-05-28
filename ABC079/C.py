from itertools import product
ABCD = input()
A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])
value = A
ans = []
op1 = ["+","-"]
op2 = ["+","-"]
op3 = ["+","-"]

op_product = list(product(op1,op2,op3))

for i in range(2):
    value = A
    if i == 0:
        value += B
    else:
        value -= B
    for j in range(2):
        if i == 0:
            value = A + B
        elif i == 1:
            value = A - B
        if j == 0:
            value += C
        else:
            value -= C
        for k in range(2):
            if i == 0 and j == 0:
                value = A + B + C
            elif i == 0 and j == 1:
                value = A + B - C
            elif i == 1 and j == 0:
                value = A - B + C
            elif i == 1 and j == 1:
                value = A - B - C
            if k == 0:
                value += D
            else:
                value -= D
            ans.append(value)

ind = ans.index(7)
ans_ope = op_product[ind]
print(str(A)+ans_ope[0]+str(B)+ans_ope[1]+str(C)+ans_ope[2]+str(D)+"=7")
