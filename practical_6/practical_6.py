# Practical 6 Chain Matrix Multiplication 

def matrix_chain(p):

    n = len(p) - 1

    # DP table
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # length = number of matrices
    for length in range(2, n + 1):

        # starting matrix
        for i in range(1, n - length + 2):

            # ending matrix
            j = i + length - 1

            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


p = [10, 20, 30, 40, 30]

print(matrix_chain(p))