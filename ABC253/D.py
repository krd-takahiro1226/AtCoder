import math
N, A, B = map(int,input().split())
a_N = N // A
b_N = N // B
AB = A*B // math.gcd(A,B) # A*Bではなく最小公倍数でないと重なって引いた位置をうまく特定できない
ab_N = N // AB

if A != B:
    N_sum = ((1+N) * N) // 2 
    A_sum = (a_N * (2*A + (a_N-1) * A)) // 2
    B_sum = (b_N * (2*B + (b_N-1) * B)) // 2
    AB_sum = (ab_N * (2*AB + (ab_N-1) * AB)) // 2
    ans = N_sum - A_sum - B_sum + AB_sum
else:
    N_sum = ((1+N) * N) // 2 
    A_sum = (a_N * (2*A + (a_N-1) * A)) // 2
    ans = N_sum - A_sum

print(ans)
