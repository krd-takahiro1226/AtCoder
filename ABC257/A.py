N, X = map(int,input().split())

syou = X // N
amari = X % N
if amari == 0:
    print(chr(syou+64))
else:
    print(chr(syou+65))
