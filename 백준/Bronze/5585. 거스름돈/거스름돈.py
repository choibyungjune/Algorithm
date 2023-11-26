money = int(input())

money = 1000 - money

lest_money = [500, 100, 50, 10, 5, 1]
cnt = 0

for lest in lest_money:
    cnt += money // lest 
    money = money % lest

print(cnt)
