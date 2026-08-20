#knapsack using 

#capacity , m  = 8  profit , p = {1,2,5,6}
# items ,  n = 4 weight , w = {2,3,4,5}             

values = [1, 2, 5, 6]
weights = [2, 3, 4, 5]
capacity = 8
dp = [[-1] * (len(weights) + 1) for _ in range(capacity + 1)]

def knapsack(capacity, n):
  if n == 0 or capacity == 0: 
    return 0
  if dp[capacity][n] != -1: 
    return dp[capacity][n]
  if weights[n-1] > capacity:
    dp[capacity][n] = knapsack(capacity, n-1)
  else:
    dp[capacity][n] = max(
      values[n-1]+knapsack(capacity - weights[n-1], n-1), 
      knapsack(capacity, n-1)
    )
  return dp[capacity][n]

print(knapsack(capacity, 4))