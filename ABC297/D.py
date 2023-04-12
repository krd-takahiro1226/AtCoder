A,B = map(int,input().split())
ans = 0
visit = False

while A != B and A != 0 and B != 0:
    visit = True
    if A > B:
        ans += A // B
        A_new = A % B
        A = A_new
    elif A < B:
        ans += B // A
        B_new = B % A
        B = B_new
if visit == True:
    print(ans - 1)
else:
    print(ans)



# シンプルにwhileで実行→TLEする
# while (A != B):
#     if A > B:
#         A = A - B
#     elif A < B:
#         B = B - A
#     ans += 1
# print(ans)
