S = input()
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
cnt = 1

for i in day_list:
    if i != S:
        cnt += 1
    else:
        print(6-cnt)
        break
