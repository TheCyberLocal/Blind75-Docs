# Problem: Climbing Stairs

### [⇦ Back to Problem Index](../../index.md)

## Textbook Problem

You are given an integer `n` representing the number of steps to reach the top of a staircase. You can climb with either `1` or `2` steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

**Example 1:**

- **Input**: n = 2
- **Output**: 2
- **Explanation**:
  1. 1 + 1 = 2
  2. 2 = 2

**Example 2:**

- **Input**: n = 3
- **Output**: 3
- **Explanation**:
  1. 1 + 1 + 1 = 3
  2. 1 + 2 = 3
  3. 2 + 1 = 3

### Constraints

- 1 <= n <= 30

---

### Approach 1: Simple Dynamic Programming

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Description**: This approach uses dynamic programming to break down the problem into subproblems, storing the results of subproblems to avoid redundant calculations. The idea is that the number of ways to reach the top can be derived from the number of ways to reach the previous step plus the number of ways to reach two steps below.
- **Algorithm**:
  1. Create an array `dp` where `dp[i]` represents the number of ways to reach step `i`.
  2. Initialize `dp[1] = 1` and `dp[2] = 2` since there is 1 way to reach step 1 and 2 ways to reach step 2.
  3. For each subsequent step `i`, set `dp[i] = dp[i-1] + dp[i-2]`.
  4. Return `dp[n]` as the result.
  ```pseudo
  function climbStairs(n):
    if n == 1:
        return 1
    dp = array of size n + 1
    dp[1] = 1
    dp[2] = 2
    for i from 3 to n:
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
  ```

---

### Approach 2: Optimized Dynamic Programming

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Description**: This is an optimized version of the dynamic programming approach. Instead of storing all previous results, it only keeps track of the last two results, which are enough to compute the next step.
- **Algorithm**:
  1. Initialize two variables, `prev1` and `prev2`, to store the number of ways to reach the previous step and the step before it, respectively.
  2. Iterate from step 3 to `n`, updating the two variables at each step.
  3. Return `prev1` after the loop, which contains the number of ways to reach step `n`.
  ```pseudo
  function climbStairs(n):
    if n == 1:
        return 1
    prev1 = 2
    prev2 = 1
    for i from 3 to n:
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1
  ```

---

### Approach 3: Fibonacci Formula

- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Description**: The problem can be related to the Fibonacci sequence, where the number of ways to climb `n` steps is equivalent to the `n`th Fibonacci number. This approach directly calculates the result using the closed-form expression (Binet’s formula).
- **Algorithm**:
  1. Use the Fibonacci formula: `Fib(n) = (phi^n - psi^n) / sqrt(5)` where `phi = (1 + sqrt(5)) / 2` and `psi = (1 - sqrt(5)) / 2`.
  2. Compute the result using this formula, rounding to the nearest integer.
  ```pseudo
  function climbStairs(n):
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    result = round((phi^n - psi^n) / sqrt(5))
    return result
  ```
