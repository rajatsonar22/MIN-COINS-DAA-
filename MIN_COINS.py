# pract no 9(b)

print(">>> MIN_COINS")
print("""This finds the minmum coins in the given list
         coins = [2,5,12,25]  """)

def min_coins(coins,target_amount):
    coins.sort(reverse = True)
    print(coins)
    coin_count = 0
    i = 0
    while target_amount > 0 and i < len (coins):
        while coins[i] <= target_amount:
            target_amount -= coins[i]
            coin_count += 1
        i += 1
    return coin_count

print("")#...space
coins = [2,5,12,25]
target_amount = 63
print(">>> Minimum number of coins required ", min_coins(coins,target_amount))
    
    
