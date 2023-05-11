S = input()
ans = 0
cnt = 0

# 下のACコードなんでREしないのか→whileに不等号が含まれていないから
# なんで不等号含まなくて良い？→ansを最大値に初期化してそこから条件指定して引いていってるから？
# ansから引く条件は、0が二回続いたときで最後の値さえ参照できれば指定必要なし→i = len(S)-1の時i+1は最後の値を参照するため、不等号いらない
while(cnt <= len(S)-1):
    if S[cnt] != "0":
        ans += 1
    else:
        if cnt + 1 <= len(S) - 1:
            if S[cnt] == S[cnt+1] == "0":
                ans += 1
                cnt += 1
            else:
                ans += 1
        else:
            ans += 1
    cnt += 1
print(ans)

# s = input()
# ans = len(s)
# i = 0
# while i < len(s) - 1:
#     if s[i] == s[i + 1] == '0':
#         ans -= 1
#         i += 1
#     i += 1
# print(ans)
