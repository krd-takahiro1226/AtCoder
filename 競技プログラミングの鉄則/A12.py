N ,K = map(int,input().split())
A = list(map(int,input().split()))

L_ind = 1
R_ind = 10**9

# countをリストに入れていくと大変だし、その記録は必要ない→1回1回目標値以上かどうか判定する
# ↑を補足すると、累積和を考える必要はない→各プリンタについて、ある時間の時何枚プリントできているかを考え、総和を取れば求まるから。
def count(A, t):
    count = 0
    for Ai in A:
        count += t // Ai
    if count >= K:
        return True
    else:
        return False

# 何回二部探索しなきゃいけない？→二部探索はwhileで回す(左端と右端が一致するまで)
# t = search_indだから、search_indによるインデックス指定でその時間の時何枚印刷しているかわかる
while L_ind < R_ind:
    search_ind = (L_ind + R_ind) // 2 
    if count(A,search_ind) == False:
        L_ind = search_ind + 1
        R_ind = R_ind
    elif count(A,search_ind) == True:
        L_ind = L_ind
        R_ind = search_ind

print(L_ind)
