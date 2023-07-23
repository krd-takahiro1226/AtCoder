N = int(input())
H = list(map(int,input().split()))
pos = 0
val = H[0]

while(pos != N-1 and H[pos+1] > H[pos]):
    pos += 1
    val = H[pos]

print(val)
