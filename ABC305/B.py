p, q = input().split()
distance = [3,1,4,1,5,9]
p_ord = ord(p)
q_ord = ord(q)

if p_ord < q_ord:
    dist = distance[p_ord-65:q_ord-65]
    print(sum(dist))
else:
    dist = distance[q_ord-65:p_ord-65]
    print(sum(dist))
