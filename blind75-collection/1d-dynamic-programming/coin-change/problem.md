# Blind75: Coin Change

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a target amount of money.

Return the fewest number of coins needed to make up the exact target amount. If it is impossible to make up the amount, return `-1`.

You may assume that you have an unlimited number of each coin.

**Example 1:**

- **Input**: `coins = [1, 5, 10]`, `amount = 12`
- **Output**: `3`
- **Explanation**:
  1. `12 = 10 + 1 + 1`
  2. The fewest coins required to make up `12` are `3`.

**Example 2:**

- **Input**: `coins = [2]`, `amount = 3`
- **Output**: `-1`
- **Explanation**: The amount `3` cannot be made up with coins of `2`.

**Example 3:**

- **Input**: `coins = [1]`, `amount = 0`
- **Output**: `0`
- **Explanation**: Choosing `0` coins is a valid way to make up `0`.

### Constraints

- `1 <= coins.length <= 10`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 1000`

---

### Approach 1: Simple Dynamic Programming

- **Time Complexity**: `O(n * m)` where `n` is the amount and `m` is the number of coins.
- **Space Complexity**: `O(n)` where `n` is the amount.
- **Description**: This approach uses dynamic programming to find the minimum number of coins required. The idea is to use a `dp` array where `dp[i]` represents the minimum number of coins needed to make up the amount `i`.
- **Algorithm**:
  1. Initialize a `dp` array of size `amount + 1` with `dp[0] = 0` and all other values set to a large number (indicating unreachable amounts).
  2. For each coin, update the `dp` array such that `dp[x] = min(dp[x], dp[x - coin] + 1)` for all `x` from the coin value to the amount.
  3. Return `dp[amount]` if it is not the initialized large number; otherwise, return `-1`.
  ```pseudo
  function coinChange(coins, amount):
    dp = array of size amount + 1 initialized to amount + 1
    dp[0] = 0
    for each coin in coins:
        for x from coin to amount:
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1
  ```
