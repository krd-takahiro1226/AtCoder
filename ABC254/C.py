N, K = map(int,input().split())
a = list(map(int,input().split()))
a_sort = sorted(a)
a_k_diff = [[] for _ in range(N)]
b = []
b_cnt = 0
ans = False

if a == a_sort or K == 1:
    ans = True
else:
    # Kズレているのを同じリストにまとめる→まとめたものの中でsort→再びくっつけ理想のものと一致するか確認
    for i in range(1,N+1):
        a_k_diff[i%K].append(a[i-1])
    for a_i in a_k_diff:
        a_i.sort()
    for j in range(1,N+1):
        b.append(a_k_diff[j%K][b_cnt])
        if j % K == 0:
            b_cnt += 1

if b == a_sort or ans:
    print("Yes")
else:
    print("No")
