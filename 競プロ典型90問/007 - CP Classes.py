import bisect
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()
# print(A)
# なぜかREが起きる →  bisect.bisect_leftを使用してright_indを求めているが、BがAのどの要素よりも大きい時、一番右に入ることになる。
# その時、right_ind = Nとなるため、ifで条件分岐しないとREになる。
for _ in range(Q):
    B = int(input())
    if N != 1:
        left_ind = bisect.bisect_left(A, B) - 1
        right_ind = bisect.bisect_left(A, B)
        if right_ind <= N - 1:
            diff = min(abs(B - A[left_ind]), abs(B - A[right_ind]))
        else:
            diff = abs(B - A[left_ind])
        print(diff)
    else:
        diff = abs(B - A[0])
        print(diff)
