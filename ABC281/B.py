S = input()

if S[0].isalpha() and S[len(S)-1].isalpha():
    if S[1:len(S)-1].isdecimal() and len(S[1:len(S)-1]) == 6:
        num = int(S[1:len(S)-1])
        if 100000 <= num <= 999999:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
