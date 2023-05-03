N, Q = map(int,input().split())
A = list(map(int,input().split()))
shift = 0

# シフトさせる系の問題は列の長さで割った余りを利用してインデックス指定
# プラス方向のシフトだけじゃなくてマイナスでも適用可能、マイナスだと逆順から配列を参照するから←正確には違う、余りが-1だったら余りに割った数を足している。
for _ in range(Q):
    T,x,y = map(int,input().split())
    if T == 1:
        tmp_x = A[(x-1-shift) % N]
        tmp_y = A[(y-1-shift) % N]
        print("x_ind",(x-1-shift) % N)
        print("y_ind",(y-1-shift) % N)
        A[(x-1-shift) % N] = tmp_y
        A[(y-1-shift) % N] = tmp_x
    elif T == 2:
        shift += 1
    else:
        print(A[(x-1-shift) % N])
# print(A)
