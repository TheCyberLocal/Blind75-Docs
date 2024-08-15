# Blind75: Coin Change

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a target amount of money.

Return the fewest number of coins needed to make up the exact target amount. If it is impossible to make up the amount, return `-1`.

You may assume that you have an unlimited number of each coin.

**Example 1:**

-   **Input**: `coins = [1, 5, 10]`, `amount = 12`
-   **Output**: `3`
-   **Explanation**:
    1. `12 = 10 + 1 + 1`
    2. The fewest coins required to make up `12` are `3`.

**Example 2:**

-   **Input**: `coins = [2]`, `amount = 3`
-   **Output**: `-1`
-   **Explanation**: The amount `3` cannot be made up with coins of `2`.

**Example 3:**

-   **Input**: `coins = [1]`, `amount = 0`
-   **Output**: `0`
-   **Explanation**: Choosing `0` coins is a valid way to make up `0`.

### Constraints

-   `1 <= len(coins) <= 10`
-   `1 <= coins[i] <= 2^31 - 1`
-   `0 <= amount <= 1000`

---

### Approach 1: Simple Dynamic Programming

-   **Time Complexity**: `O(n * m)` where `n` is the amount and `m` is the number of coins.
-   **Space Complexity**: `O(n)` where `n` is the amount.
-   **Description**: This approach utilizes dynamic programming to determine the minimum number of coins required to achieve the target amount. The idea is to maintain an array where each element represents the fewest coins needed to make up the amount of the index integer. We will initialize every value in the array to a number that is unreachable, indicating that it is impossible to make up that amount. However, the first element should be set to zero, as no coins are needed to make up the amount zero. For each coin in the given set of coins, the algorithm iterates through the array starting from the value of the coin up to the target amount. During each iteration, it updates the current value in the array by comparing it with the value that represents the minimum number of coins needed to make up the amount minus the current coin value. This way, we progressively build up the solution, ensuring that the array holds the smallest number of coins required to make up each amount from zero to the target amount. Finally, we check the value corresponding to the target amount. If it remains unchanged (indicating that it’s still in an unreachable state), we return `-1`. Otherwise, we return the value, representing the fewest number of coins needed to make up the amount.
- **Algorithm**:

    1. **Initialization**: Create an array `dp` with a size of `amount + 1`. Set the first element `dp[0]` to `0`, representing that zero coins are needed to achieve an amount of zero. Set all other elements to a large value, indicating that these amounts are initially unreachable.

    2. **Iterate Through Coins**: For each coin in the `coins` array, consider that this coin could contribute to making up various amounts. For each possible amount starting from the coin's value up to the target `amount`, evaluate whether using this coin would reduce the number of coins needed to achieve that amount.

    3. **Update the Array**: For each possible amount that can be formed with the current coin, update the corresponding value in the `dp` array. Specifically, check if using the current coin results in a smaller number of coins required compared to the current value stored in `dp`. If it does, update the value in the `dp` array to reflect this new minimum.

    4. **Determine the Result**: After processing all the coins, examine the value at `dp[amount]`. If it remains as the large value initialized earlier, it means that the target amount cannot be reached with the given coins, so return `-1`. Otherwise, return the value at `dp[amount]`, which represents the fewest coins needed to make up the target amount.

```pseudo
function coinChange(coins, amount):
    dp = array of size amount + 1 initialized to amount + 1
    dp[0] = 0

    for each coin in coins:
        for x from coin to amount:
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
```
