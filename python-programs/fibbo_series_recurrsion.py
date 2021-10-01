def rec_fibbo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return rec_fibbo(num - 1) + rec_fibbo(num - 2)

num = 5
for i in range(0, num):
    print(rec_fibbo(i))
