def knapSack(W, wt, val, n):
    # Create a 2D DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],  # include the item
                    dp[i - 1][w]                            # exclude the item
                )
            else:
                dp[i][w] = dp[i - 1][w]  # item too heavy

    return dp[n][W]  # maximum profit


# ---- Main Code ----
n = int(input("Enter number of items: "))

val = list(map(int, input("Enter values (profits) of items: ").split()))
wt = list(map(int, input("Enter weights of items: ").split()))
W = int(input("Enter capacity of knapsack: "))

maxProfit = knapSack(W, wt, val, n)
print("\nMaximum profit =", maxProfit)
