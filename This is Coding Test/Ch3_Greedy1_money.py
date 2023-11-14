n = 1260

coins = [500, 100, 50, 10]
total = 0

for coin in coins:
    total += n // coin
    n %= coin
    
print(total)


#O(K)