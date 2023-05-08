N = int(input())
record = set()
ans_cnt = 0

for _ in range(N):
    S = input()
    if S[0] in ["H", "D", "C", "S"]:
        if S[1] in ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']:
            if S not in record:
                ans_cnt += 1
                record.add(S)

if ans_cnt == N:
    print("Yes")
else:
    print("No")
