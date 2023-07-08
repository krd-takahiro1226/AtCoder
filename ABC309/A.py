A, B = map(int,input().split())
diff = B - A
A_amari = A % 3

if A_amari != 0 and diff == 1:
    print('Yes')
else:
    print('No')
