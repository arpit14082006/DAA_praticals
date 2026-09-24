# Practical 7
# Making Change Problem using Dynamic Programming

def min_coins(coins, amount):

    # dp[i] = minimum coins required to make amount i
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    # Build the DP table
    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# Input
coins = [1, 2, 5, 10]
amount = 18

# Find minimum number of coins
result = min_coins(coins, amount)

print("Coins:", coins)
print("Amount:", amount)
print("Minimum number of coins required:", result)